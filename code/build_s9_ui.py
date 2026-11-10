"""build_s9_ui.py — sklada jednoplikowa strone do przesiewu listy NICE (Suplement S9).

Wejscie : data/external/S9_nice_screen.csv (247 tytulow NICE IPG)
Wyjscie : code/s9_ui.html (dane wbudowane, dziala offline, nic nie wysyla)
Strona nie pokazuje niczego z materialu 48 — ortopeda mapuje tytuly na frazy bez niego.
"""
from __future__ import annotations
import csv, json
from pathlib import Path

ROWS = list(csv.DictReader(open("data/external/S9_nice_screen.csv", encoding="utf-8-sig")))
COLS = list(ROWS[0])
ROWS.sort(key=lambda r: (int(r["year"]), int(r["ipg"][3:])))

HTML = """<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>S9 — przesiew NICE IPG</title>
<style>
:root{--bg:#fbfbfa;--surface:#fff;--ink:#1a1a18;--ink2:#4a4a46;--ink3:#78786f;--line:#e4e4df;
 --accent:#3d6b8f;--ok:#2e6b4f;--bad:#8a3a3a;--chip:#eef2f5}
@media (prefers-color-scheme:dark){:root{--bg:#161614;--surface:#1e1e1c;--ink:#f0efec;--ink2:#c2c1bb;
 --ink3:#8a8a82;--line:#33332f;--accent:#7fb0d4;--ok:#7fc0a0;--bad:#d99a9a;--chip:#262623}}
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
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--ink3);font-weight:600}
td.num{color:var(--ink2);font-variant-numeric:tabular-nums;white-space:nowrap}
.title{font-weight:600}
.title a{color:inherit;text-decoration:none}
.title a:hover{text-decoration:underline}
input[type=text]{font:inherit;background:var(--bg);color:var(--ink);border:1px solid var(--line);
 border-radius:6px;padding:3px 6px;font-size:13px;width:100%}
input[type=text]:disabled{opacity:.35}
textarea{width:100%;font-family:ui-monospace,Consolas,monospace;font-size:12px;min-height:240px;
 background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:6px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:13px;margin:14px 0}
.pick{white-space:nowrap}
.pick button{padding:2px 9px;font-size:12px}
.yes.on{background:var(--ok);border-color:transparent}
.no.on{background:var(--bad);border-color:transparent}
.tagchip{background:var(--chip);border-radius:20px;padding:1px 8px;font-size:11.5px;color:var(--ink2);white-space:nowrap}
tr.done td{background:color-mix(in srgb,var(--surface) 92%,var(--ok))}
</style></head><body>
<header>
 <div class="row">
  <h1>S9 — przesiew NICE Interventional Procedures</h1>
  <span class="muted" id="cnt"></span>
  <span style="flex:1"></span>
  <button id="save" class="primary">Zapisz CSV</button>
  <button id="show">Pokaz CSV</button>
 </div>
 <div class="row" style="margin-top:6px" id="filters"></div>
</header>
<main>
 <div class="card">
  <b>Dla kazdego tytulu:</b> <b>tak</b> (procedura ortopedyczna) albo <b>nie</b>.
  Przy <b>tak</b> wpisz <b>wszystkie nazwy</b>, pod ktorymi technologia wystepuje w abstraktach,
  rozdzielone srednikami — pelna nazwe, skrot i warianty, np.
  <i>percutaneous vertebroplasty; vertebroplasty; pvp</i>. Policzone beda razem.
  Jesli nie ma odpowiednika w literaturze, kliknij <b>brak odpowiednika</b>.
  Etykieta <span class="tagchip">other specialty?</span> to tylko propozycja — decydujesz Ty.
  Nie zagladaj przy tym do materialu 48. Postep zapisuje sie w przegladarce; na koniec
  <b>Zapisz CSV</b>. Tytul prowadzi do strony NICE.
 </div>
 <table id="tbl"></table>
 <div class="card" id="csvbox" hidden>
  <h3 style="margin:0 0 6px;font-size:13px">CSV — Ctrl+A, Ctrl+C</h3>
  <textarea id="csvout"></textarea>
 </div>
</main>
<script>
"use strict";
var ROWS = __ROWS__;
var COLS = __COLS__;
var BRAK = "brak odpowiednika";
var filtr = "todo";
var $ = function(s){ return document.querySelector(s); };
function stash(){ try{ localStorage.setItem("s9_nice", JSON.stringify(
  ROWS.map(function(x){ return [x.ipg, x.ortopedia_PC, x.fraza_PC, x.uwaga_PC]; }))); }catch(e){} }
function restore(){ try{ var s = JSON.parse(localStorage.getItem("s9_nice")||"null"); if(!s) return;
  var by = {}; s.forEach(function(a){ by[a[0]] = a; });
  ROWS.forEach(function(r){ var a = by[r.ipg]; if(a){ r.ortopedia_PC = a[1]||""; r.fraza_PC = a[2]||""; r.uwaga_PC = a[3]||""; } });
  }catch(e){} }
function done(r){ return r.ortopedia_PC === "nie" || (r.ortopedia_PC === "tak" && r.fraza_PC.trim()); }
var FILTRY = [["todo","do zrobienia",function(r){ return !done(r); }],
              ["wszystkie","wszystkie",function(){ return true; }],
              ["tak","tak",function(r){ return r.ortopedia_PC==="tak"; }],
              ["nie","nie",function(r){ return r.ortopedia_PC==="nie"; }],
              ["prop","z propozycja",function(r){ return !!r.propozycja_modelu; }],
              ["bezprop","bez propozycji",function(r){ return !r.propozycja_modelu; }]];
function chips(){
  $("#filters").innerHTML = FILTRY.map(function(f){
    var n = ROWS.filter(f[2]).length;
    return '<button data-k="'+f[0]+'" class="'+(filtr===f[0]?"on":"")+'">'+f[1]+' <span class="muted">'+n+'</span></button>'; }).join(""); }
function esch(v){ return String(v==null?"":v).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/"/g,"&quot;"); }
function draw(){
  var test = FILTRY.filter(function(f){ return f[0]===filtr; })[0][2];
  var v = ROWS.filter(test);
  $("#tbl").innerHTML = '<tr><th>rok</th><th>IPG</th><th>tytul NICE</th><th>ortopedia?</th>'
    + '<th style="width:32%">nazwy w abstraktach (srednik)</th><th style="width:14%">uwaga</th></tr>' + v.map(function(r){
    var i = ROWS.indexOf(r), tak = r.ortopedia_PC === "tak";
    return '<tr class="'+(done(r)?"done":"")+'"><td class="num">'+r.year+'</td><td class="num">'+r.ipg+'</td>'
     + '<td><div class="title"><a href="https://www.nice.org.uk/guidance/'+r.htg.toLowerCase()+'" target="_blank" rel="noopener">'+esch(r.title)+'</a></div>'
     + '<div class="muted">'+esch(r.nice_topic)+(r.propozycja_modelu?' <span class="tagchip">'+esch(r.propozycja_modelu)+'</span>':'')+'</div></td>'
     + '<td><div class="pick"><button class="yes'+(tak?" on":"")+'" data-i="'+i+'" data-v="tak">tak</button> '
     + '<button class="no'+(r.ortopedia_PC==="nie"?" on":"")+'" data-i="'+i+'" data-v="nie">nie</button></div></td>'
     + '<td><input type="text" data-i="'+i+'" data-f="fraza_PC" value="'+esch(r.fraza_PC)+'"'+(tak?"":" disabled")+'>'
     + (tak?'<button style="margin-top:4px;padding:1px 7px;font-size:11.5px" data-i="'+i+'" data-brak="1">'+BRAK+'</button>':'')+'</td>'
     + '<td><input type="text" data-i="'+i+'" data-f="uwaga_PC" value="'+esch(r.uwaga_PC)+'"></td></tr>'; }).join("");
  var nd = ROWS.filter(done).length;
  $("#cnt").textContent = "zrobione " + nd + " z " + ROWS.length + " | tak " + ROWS.filter(function(r){ return r.ortopedia_PC==="tak"; }).length;
  chips(); }
document.addEventListener("click", function(e){
  var b = e.target.closest("button"); if(!b) return;
  if(b.dataset.k){ filtr = b.dataset.k; draw(); return; }
  if(b.dataset.brak){ ROWS[+b.dataset.i].fraza_PC = BRAK; stash(); draw(); return; }
  if(b.dataset.v){ var r = ROWS[+b.dataset.i];
    r.ortopedia_PC = r.ortopedia_PC === b.dataset.v ? "" : b.dataset.v;
    if(r.ortopedia_PC !== "tak") r.fraza_PC = "";
    stash(); draw();
    if(r.ortopedia_PC === "tak"){ var t = document.querySelector('input[data-i="'+b.dataset.i+'"][data-f="fraza_PC"]'); if(t) t.focus(); } } });
// zapis przy kazdym znaku, przerysowanie dopiero po wyjsciu z pola (filtr "do zrobienia" nie zabiera wiersza w trakcie pisania)
document.addEventListener("input", function(e){ var t = e.target; if(!t.dataset || !t.dataset.f) return;
  ROWS[+t.dataset.i][t.dataset.f] = t.value; stash(); });
document.addEventListener("change", function(e){ if(e.target.dataset && e.target.dataset.f) draw(); });
function esc(v){ v = v==null?"":String(v); return /[",\\n\\r]/.test(v) ? '"'+v.replace(/"/g,'""')+'"' : v; }
function buildCSV(){
  return COLS.join(",") + "\\n" + ROWS.map(function(r){
    return COLS.map(function(c){ return esc(r[c]); }).join(","); }).join("\\n") + "\\n"; }
$("#save").onclick = function(){ var b = new Blob(["\\ufeff"+buildCSV()],{type:"text/csv;charset=utf-8"});
  var a = document.createElement("a"); a.href = URL.createObjectURL(b);
  a.download = "S9_nice_screen_PC_"+new Date().toISOString().slice(0,10)+".csv"; a.click();
  setTimeout(function(){ URL.revokeObjectURL(a.href); },2000); };
$("#show").onclick = function(){ var b = $("#csvbox"); b.hidden = false;
  var t = $("#csvout"); t.value = buildCSV(); t.focus(); t.select(); b.scrollIntoView({behavior:"smooth"}); };
restore(); draw();
</script></body></html>
"""

out = (HTML.replace("__ROWS__", json.dumps(ROWS, ensure_ascii=False, separators=(",", ":")))
       .replace("__COLS__", json.dumps(COLS)))
Path("code/s9_ui.html").write_text(out, encoding="utf-8")
print("code/s9_ui.html:", len(out), "znakow,", len(ROWS), "wierszy")
