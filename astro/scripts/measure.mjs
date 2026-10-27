import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
function walk(dir, out=[]) { for (const n of fs.readdirSync(dir)) { const p=path.join(dir,n); const s=fs.statSync(p); if(s.isDirectory()) walk(p,out); else out.push(p);} return out; }
const files=walk("dist");
let total=0, gz=0;
const rows=[];
for(const f of files){ const b=fs.readFileSync(f); total+=b.length; if(/\.(js|css|html|json|xml|svg)$/.test(f)) gz += zlib.gzipSync(b,{level:9}).length; }
console.log("dist files", files.length, "raw MB", (total/1048576).toFixed(2), "gzip MB", (gz/1048576).toFixed(2));
const js=files.filter(f=>f.endsWith(".js")).map(f=>{const b=fs.readFileSync(f); return {f:path.basename(f),raw:b.length,gz:zlib.gzipSync(b,{level:9}).length};}).sort((a,b)=>b.raw-a.raw);
console.log("JS chunks", JSON.stringify(js.slice(0,12),null,2));
const pf=files.filter(f=>f.includes("pagefind")); let pRaw=0; for(const f of pf) pRaw+=fs.statSync(f).size; console.log("pagefind files",pf.length,"raw KB",(pRaw/1024).toFixed(1));
const home=fs.readFileSync("dist/index.html","utf8"); const lab=fs.readFileSync("dist/analytic-geometry/lab/index.html","utf8");
for(const [name,html] of [["home",home],["lab",lab]]) { const chunks=[...html.matchAll(/src="([^"]+\.js)"/g)].map(m=>m[1].split("/").pop()); console.log(name,"scripts",JSON.stringify([...new Set(chunks)])); }
const mk="..\\site\\search\\search_index.json"; if(fs.existsSync(mk)) console.log("mkdocs search index MB",(fs.statSync(mk).size/1048576).toFixed(2));
