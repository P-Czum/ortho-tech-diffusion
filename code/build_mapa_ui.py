"""build_mapa_ui.py — sklada jednoplikowa strone do walidacji mapy fraz.

Wejscie : data/processed/np_mapa_propozycja.csv (813 wierszy, propozycja kategorii)
Wyjscie : code/mapa_ui.html (dane wbudowane, dziala offline, nic nie wysyla)
"""
from __future__ import annotations
import csv, json
from pathlib import Path

ROWS = list(csv.DictReader(open("data/processed/np_mapa_propozycja.csv", encoding="utf-8")))
for r in ROWS:
    r["pozycja"] = int(r["pozycja"]); r["n"] = int(r["n"])
    r["prevalence_pct"] = float(r["prevalence_pct"])
    r["na_mapie"] = r["na_mapie"] == "True"
    r["w_rdzeniu_4"] = r["w_rdzeniu_4"] == "True"

HTML = """<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mapa fraz wschodzacych — walidacja</title>
<style>
:root{--bg:#fbfbfa;--surface:#fff;--ink:#1a1a18;--ink2:#4a4a46;--ink3:#78786f;--line:#e4e4df;
 --accent:#3d6b8f;--ok:#2e6b4f;--warn:#8a5a1f;--bad:#8a3a3a;--chip:#eef2f5}
@media (prefers-color-scheme:dark){:root{--bg:#161614;--surface:#1e1e1c;--ink:#f0efec;--ink2:#c2c1bb;
 --ink3:#8a8a82;--line:#33332f;--accent:#7fb0d4;--ok:#7fc0a0;--warn:#d6a860;--bad:#d99a9a;--chip:#262623}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif}
header{position:sticky;top:0;z-index:6;background:var(--surface);border-bottom:1px solid var(--line);padding:9px 14px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
h1{font-size:13.5px;margin:0 8px 0 0;font-weight:600}
button{font:inherit;border:1px solid var(--line);background:var(--surface);color:var(--ink);
 padding:4px 10px;border-radius:7px;cursor:pointer;font-size:13px}
button:hover{border-color:var(--accent)}
button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
button.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
.muted{color:var(--ink3);font-size:12.5px}
main{max-width:1240px;margin:0 auto;padding:14px 14px 90px}
table{border-collapse:collapse;width:100%;background:var(--surface);border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:middle}
th{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--ink3);font-weight:600}
td.num{text-align:right;color:var(--ink2);font-variant-numeric:tabular-nums;white-space:nowrap}
.term{font-weight:600}
.var{color:var(--ink3);font-weight:400;font-size:12px}
select,textarea,input[type=text]{font:inherit;background:var(--bg);color:var(--ink);
 border:1px solid var(--line);border-radius:6px;padding:3px 6px;font-size:13px}
textarea{width:100%;min-height:90px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:13px;margin:14px 0}
.pick button{padding:2px 7px;font-size:12px}
.t1.on{background:var(--ok);border-color:transparent}
.t2.on{background:var(--warn);border-color:transparent}
.t3.on{background:var(--bad);border-color:transparent}
.tagchip{background:var(--chip);border-radius:20px;padding:1px 8px;font-size:11.5px;color:var(--ink2);white-space:nowrap}
</style></head><body>
<header>
 <div class="row">
  <h1>Mapa fraz wschodzacych — ortopedia 2005-2025</h1>
  <button id="tab-mapa" class="on">Mapa</button>
  <button id="tab-odrzucone">Odrzucone</button>
  <span class="muted" id="cnt"></span>
  <span style="flex:1"></span>
  <button id="save" class="primary">Zapisz CSV</button>
  <button id="copy">Kopiuj</button>
  <button id="show">Pokaz CSV</button>
 </div>
 <div class="row" style="margin-top:6px" id="filters"></div>
 <div class="row" style="margin-top:6px">
  <label class="muted"><input type="checkbox" id="hidevar" checked> ukryj skroty i warianty tego samego pojecia</label>
  <label class="muted"><input type="checkbox" id="lim100" checked> pokaz tylko 100 pierwszych</label>
  <span class="muted" style="margin-left:10px">dolacz:</span>
  <label class="muted"><input type="checkbox" id="opt-lek"> leki (kontrast)</label>
  <label class="muted"><input type="checkbox" id="opt-rozpoznanie"> rozpoznania (druga praca)</label>
  <label class="muted"><input type="checkbox" id="opt-parametr"> parametry radiologiczne</label>
  <label class="muted"><input type="checkbox" id="opt-czynnik"> czynniki pacjenta</label>
  <label class="muted"><input type="checkbox" id="opt-organizacja"> organizacja opieki</label>
  <label class="muted"><input type="checkbox" id="opt-niejasne"> niejasne</label>
 </div>
</header>
<main>
 <div class="card" id="intro">
  <b>Co tu jest.</b> 813 fraz, ktore spelniaja kryterium wylonienia w trzech wariantach tekstu
  (primary, streszczenia, angielski). Kazdej przypisalem <b>proponowana kategorie</b> — popraw ja,
  jesli sie myle. Mapa pokazuje tylko <b>rozpoznania, techniki leczenia, technologie i leki</b>.
  Skale, kwestionariusze, wyniki i metody badawcze sa odsiane i siedza w zakladce
  <b>Odrzucone</b>; jesli cos tam wpadlo niesluszne, zmien mu kategorie i wroci na mape.
  Skroty (CLTI, TXA, PJK) sa sklejone z pelnymi formami i domyslnie ukryte.
  <br><b>Trafnosc</b> oceniaj tylko tam, gdzie masz zdanie: trafna / watpliwa / bledna.
 </div>
 <table id="tbl"></table>
 <div class="card">
  <h3 style="margin:0 0 6px;font-size:13px">Czego brakuje</h3>
  <p class="muted" style="margin:0 0 8px">Co wylonilo sie w ortopedii w tym okresie, a nie ma tego na liscie?
  Jedna pozycja na linie, w miare mozliwosci z przyblizonym rokiem.</p>
  <textarea id="missing" placeholder="np. vancomycin powder — ok. 2014"></textarea>
 </div>
 <div class="card" id="csvbox" hidden>
  <h3 style="margin:0 0 6px;font-size:13px">CSV — Ctrl+A, Ctrl+C</h3>
  <textarea id="csvout" style="min-height:240px;font-family:ui-monospace,Consolas,monospace;font-size:12px"></textarea>
 </div>
</main>
<script>
"use strict";
var ROWS = __ROWS__;
var KAT = ["rozpoznanie","technika","technologia","lek","parametr","czynnik","organizacja","niejasne","skala","wynik","metoda","artefakt"];
var RDZEN = {technika:1,technologia:1};
var OPCJE = ["lek","rozpoznanie","parametr","czynnik","organizacja","niejasne"];
function MAPAset(){ var m={}; Object.keys(RDZEN).forEach(function(k){m[k]=1});
 OPCJE.forEach(function(k){ var c=document.getElementById("opt-"+k); if(c&&c.checked) m[k]=1; });
 return m; }
var TRAF = ["trafna","watpliwa","bledna"];
var tab = "mapa", filtr = null;
ROWS.forEach(function(r){ r.kategoria_ocena = r.kategoria; r.trafnosc = ""; r.uwaga = ""; });
var $ = function(s){ return document.querySelector(s); };
function stash(){ try{ localStorage.setItem("np_mapa", JSON.stringify({
  r: ROWS.map(function(x){ return [x.term, x.kategoria_ocena, x.trafnosc, x.uwaga]; }),
  m: $("#missing").value })); }catch(e){} }
function restore(){ try{ var s = JSON.parse(localStorage.getItem("np_mapa")||"null"); if(!s) return;
  var by={}; (s.r||[]).forEach(function(a){ by[a[0]]=a; });
  ROWS.forEach(function(r){ var a=by[r.term]; if(a){ r.kategoria_ocena=a[1]||r.kategoria; r.trafnosc=a[2]||""; r.uwaga=a[3]||""; } });
  if(s.m) $("#missing").value = s.m; }catch(e){} }
function visible(){
  var M = MAPAset();
  var v = ROWS.filter(function(r){
    var na = !!M[r.kategoria_ocena];
    if(tab==="mapa" ? !na : na) return false;
    if(tab==="mapa" && $("#hidevar").checked && r.wariant_do) return false;
    if(filtr && r.kategoria_ocena !== filtr) return false;
    return true; });
  if(tab==="mapa" && $("#lim100").checked) v = v.slice(0,100);
  return v; }
function chips(){
  var c = {}; ROWS.forEach(function(r){ c[r.kategoria_ocena]=(c[r.kategoria_ocena]||0)+1; });
  $("#filters").innerHTML = '<button data-k="" class="'+(filtr?"":"on")+'">wszystkie</button>' +
    KAT.filter(function(k){ return c[k]; }).map(function(k){
      return '<button data-k="'+k+'" class="'+(filtr===k?"on":"")+'">'+k+' <span class="muted">'+c[k]+'</span></button>'; }).join(""); }
function draw(){
  var v = visible();
  $("#tbl").innerHTML = '<tr><th>#</th><th>fraza</th><th class="num">y&#8320;</th><th class="num">2021-25</th>'
    + '<th>kategoria</th><th>trafnosc</th><th>uwaga</th></tr>' + v.map(function(r){
    var i = ROWS.indexOf(r);
    return '<tr><td class="num">'+r.pozycja+'</td>'
     + '<td><span class="term">'+r.term+'</span>'+(r.wariant_do?' <span class="var">= '+r.wariant_do+'</span>':'')
     + (r.w_rdzeniu_4?' <span class="tagchip">rdzen 47</span>':'')+'</td>'
     + '<td class="num">'+r.y0+'</td><td class="num">'+r.prevalence_pct.toFixed(3)+'%</td>'
     + '<td><select data-i="'+i+'" data-f="kategoria_ocena">'+KAT.map(function(k){
         return '<option'+(r.kategoria_ocena===k?" selected":"")+'>'+k+'</option>'; }).join("")+'</select></td>'
     + '<td><div class="pick">'+TRAF.map(function(t,j){
         return '<button class="t'+(j+1)+(r.trafnosc===t?" on":"")+'" data-i="'+i+'" data-f="trafnosc" data-v="'+t+'">'+t+'</button>'; }).join("")+'</div></td>'
     + '<td><input type="text" data-i="'+i+'" data-f="uwaga" value="'+(r.uwaga||"").replace(/"/g,"&quot;")+'" style="width:140px"></td></tr>'; }).join("");
  var M2 = MAPAset();
  var onmap = ROWS.filter(function(r){ return M2[r.kategoria_ocena] && !r.wariant_do; }).length;
  var ocen = ROWS.filter(function(r){ return r.trafnosc; }).length;
  $("#cnt").textContent = "widocznych " + v.length + " | na mapie po scaleniu " + onmap + " | ocenionych " + ocen;
  $("#intro").hidden = tab !== "mapa"; chips(); }
document.addEventListener("click", function(e){
  var b = e.target.closest("button"); if(!b) return;
  if(b.id==="tab-mapa"||b.id==="tab-odrzucone"){ tab = b.id==="tab-mapa"?"mapa":"odrzucone";
    $("#tab-mapa").classList.toggle("on",tab==="mapa"); $("#tab-odrzucone").classList.toggle("on",tab!=="mapa"); draw(); return; }
  if(b.dataset.k !== undefined){ filtr = b.dataset.k || null; draw(); return; }
  if(b.dataset.f === "trafnosc"){ var r = ROWS[+b.dataset.i];
    r.trafnosc = r.trafnosc === b.dataset.v ? "" : b.dataset.v; stash(); draw(); } });
document.addEventListener("change", function(e){ var t = e.target;
  if(t.id==="hidevar"||t.id==="lim100"||t.id.indexOf("opt-")===0){ draw(); return; }
  if(!t.dataset || !t.dataset.f) return;
  ROWS[+t.dataset.i][t.dataset.f] = t.value; stash(); draw(); });
document.addEventListener("input", function(e){ if(e.target.id==="missing") stash(); });
function esc(v){ v = v==null?"":String(v); return /[",\\n\\r]/.test(v) ? '"'+v.replace(/"/g,'""')+'"' : v; }
function buildCSV(){
  var head = ["pozycja","term","y0","prevalence_pct","kategoria_proponowana","kategoria_ocena","wariant_do","trafnosc","uwaga"];
  var s = head.join(",") + "\\n" + ROWS.map(function(r){
    return [r.pozycja,r.term,r.y0,r.prevalence_pct,r.kategoria,r.kategoria_ocena,r.wariant_do,r.trafnosc,r.uwaga].map(esc).join(","); }).join("\\n");
  return s + "\\n# BRAKUJACE\\n" + ($("#missing").value||"").split(/\\n/).map(esc).join("\\n"); }
$("#save").onclick = function(){ var b = new Blob(["\\ufeff"+buildCSV()],{type:"text/csv;charset=utf-8"});
  var a = document.createElement("a"); a.href = URL.createObjectURL(b);
  a.download = "ocena_mapy_"+new Date().toISOString().slice(0,10)+".csv"; a.click();
  setTimeout(function(){ URL.revokeObjectURL(a.href); },2000); };
$("#copy").onclick = function(){ navigator.clipboard.writeText(buildCSV()).then(function(){
  $("#copy").textContent = "skopiowane"; setTimeout(function(){ $("#copy").textContent = "Kopiuj"; },1500); }); };
$("#show").onclick = function(){ var b = $("#csvbox"); b.hidden = false;
  var t = $("#csvout"); t.value = buildCSV(); t.focus(); t.select(); b.scrollIntoView({behavior:"smooth"}); };
restore(); draw();
</script></body></html>
"""

out = HTML.replace("__ROWS__", json.dumps(ROWS, ensure_ascii=False, separators=(",", ":")))
Path("code/mapa_ui.html").write_text(out, encoding="utf-8")
print("code/mapa_ui.html:", len(out), "znakow,", len(ROWS), "wierszy")
