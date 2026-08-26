"""medline_fetch.py — lustro MEDLINE/PubMed baseline + updatefiles.

Pobiera pubmed26nXXXX.xml.gz z https://ftp.ncbi.nlm.nih.gov/pubmed/{baseline,updatefiles}/,
weryfikuje sumy MD5, zapisuje pod --dest. Wznawialny — plik z poprawnym MD5 jest pomijany
bez ponownego pobierania.

Uruchom z Windows: python code/medline_fetch.py --dest D:/medline_2026
"""
from __future__ import annotations
import argparse, hashlib, logging, re, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

BASE_URL = "https://ftp.ncbi.nlm.nih.gov/pubmed"
SETS = ("baseline", "updatefiles")
UA = {"User-Agent": "medline-mirror/1.0 (research; contact: przemek.czuma@gmail.com)"}
FILE_RE = re.compile(r'href="(pubmed\d{2}n\d{4}\.xml\.gz)"')


def setup_logging(dest: Path) -> str:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (dest / "logs").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(dest / "logs" / f"fetch_{run_id}.log", encoding="utf-8"),
                  logging.StreamHandler(sys.stdout)])
    return run_id


def http_get(url: str, timeout: int = 180, retries: int = 3) -> bytes:
    """FTP NCBI po HTTPS bywa kapryzny — ok. 1/3 zadan konczy sie URLError albo
    RemoteDisconnected. Bez retry padal listing (koniec runu) albo pobranie .md5
    (plik przyjmowany bez weryfikacji sumy)."""
    for attempt in range(1, retries + 1):
        try:
            with urlopen(Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception:
            if attempt == retries:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("nieosiagalne")


def list_remote(subset: str) -> list[str]:
    html = http_get(f"{BASE_URL}/{subset}/", timeout=120).decode("utf-8", "replace")
    return sorted(set(FILE_RE.findall(html)))


def md5_of(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        while block := fh.read(chunk):
            h.update(block)
    return h.hexdigest()


def expected_md5(subset: str, name: str) -> str | None:
    """NCBI publishes '<name>.md5' containing 'MD5(<name>)= <hex>'."""
    try:
        txt = http_get(f"{BASE_URL}/{subset}/{name}.md5", timeout=60).decode()
    except Exception:
        return None
    m = re.search(r"=\s*([0-9a-f]{32})", txt)
    return m.group(1) if m else None


def fetch_one(subset: str, name: str, dest: Path, retries: int = 3) -> tuple[str, str]:
    """Zwraca (status, szczegol). status: ok | skip | error"""
    out = dest / subset / name
    out.parent.mkdir(parents=True, exist_ok=True)
    want = expected_md5(subset, name)

    if out.exists():
        if want is None or md5_of(out) == want:
            return "skip", name
        logging.warning(f"  {name}: MD5 nie zgadza sie z lokalnym plikiem, pobieram ponownie")

    for attempt in range(1, retries + 1):
        try:
            data = http_get(f"{BASE_URL}/{subset}/{name}")
            if want and hashlib.md5(data).hexdigest() != want:
                raise ValueError("MD5 mismatch po pobraniu")
            tmp = out.with_suffix(out.suffix + ".part")
            tmp.write_bytes(data)
            tmp.replace(out)
            return "ok", f"{name} ({len(data)/1024/1024:.1f} MB)"
        except Exception as exc:
            if attempt == retries:
                return "error", f"{name}: {type(exc).__name__}: {exc}"
            time.sleep(2 ** attempt)
    return "error", name


def main() -> int:
    ap = argparse.ArgumentParser(description="Lustro MEDLINE baseline + updatefiles.")
    ap.add_argument("--dest", required=True, help=r"katalog docelowy, np. D:\medline_2026")
    ap.add_argument("--sets", default=",".join(SETS), help="baseline,updatefiles")
    ap.add_argument("--workers", type=int, default=4,
                    help="rownolegle pobierania; NCBI prosi o umiar (domyslnie 4)")
    ap.add_argument("--limit", type=int, help="pobierz najwyzej N plikow (do testu)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dest = Path(args.dest).expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)
    run_id = setup_logging(dest)
    logging.info(f"START run_id={run_id} dest={dest}")

    jobs: list[tuple[str, str]] = []
    for subset in [s.strip() for s in args.sets.split(",") if s.strip()]:
        names = list_remote(subset)
        logging.info(f"{subset}: {len(names)} plikow na serwerze")
        jobs += [(subset, n) for n in names]

    have = {(s, p.name) for s in SETS for p in (dest / s).glob("*.xml.gz")}
    todo = [j for j in jobs if j not in have]
    logging.info(f"lokalnie: {len(have)} | do sprawdzenia/pobrania: {len(todo)}")
    if args.limit:
        todo = todo[: args.limit]

    if args.dry_run:
        for s, n in todo[:50]:
            print(f"[dry] {s}/{n}")
        logging.info(f"--dry-run: {len(todo)} plikow do pobrania")
        return 0

    counts = {"ok": 0, "skip": 0, "error": 0}
    errors: list[str] = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_one, s, n, dest): (s, n) for s, n in todo}
        for i, fut in enumerate(as_completed(futures), 1):
            status, detail = fut.result()
            counts[status] += 1
            if status == "error":
                errors.append(detail); logging.error(f"  ! {detail}")
            if i % 25 == 0 or i == len(todo):
                el = time.time() - t0
                logging.info(f"  [{i}/{len(todo)}] ok={counts['ok']} skip={counts['skip']} "
                             f"err={counts['error']} eta={(len(todo)-i)/(i/el)/60:.1f} min")

    logging.info(f"END {counts} elapsed={(time.time()-t0)/60:.1f} min")
    if errors:
        (dest / "logs" / f"fetch_errors_{run_id}.txt").write_text("\n".join(errors), encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
