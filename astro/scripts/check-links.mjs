import fs from "node:fs";
import path from "node:path";

const dist = path.resolve("dist");
const base = "/YanYu-Site";
const files = [];
function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) walk(full);
    else if (name.endsWith(".html")) files.push(full);
  }
}
walk(dist);

const broken = new Map();
const seen = new Set();
for (const file of files) {
  const html = fs.readFileSync(file, "utf8");
  for (const m of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    let url = m[1];
    if (!url.startsWith(base)) continue;
    url = url.slice(base.length) || "/";
    url = url.split("#")[0].split("?")[0];
    if (!url) continue;
    let decoded;
    try {
      decoded = decodeURIComponent(url);
    } catch {
      decoded = url;
    }
    let target;
    if (decoded.endsWith("/")) target = path.join(dist, decoded, "index.html");
    else if (path.extname(decoded)) target = path.join(dist, decoded);
    else target = path.join(dist, decoded, "index.html");
    if (fs.existsSync(target) && fs.statSync(target).isFile()) continue;
    const key = `${path.relative(dist, file)} -> ${url}`;
    if (!seen.has(key)) {
      seen.add(key);
      broken.set(key, true);
    }
  }
}

const all = [...broken.keys()];
console.log(JSON.stringify({ htmlFiles: files.length, broken: all.length, sample: all.slice(0, 40) }, null, 2));
if (all.length) process.exitCode = 1;
