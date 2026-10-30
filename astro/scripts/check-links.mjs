import fs from "node:fs";
import path from "node:path";

const dist = path.resolve("dist");
const base = "/YanYu-Site";
const files = [];
const allFiles = [];
function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) walk(full);
    else {
      allFiles.push(full);
      if (name.endsWith(".html")) files.push(full);
    }
  }
}
walk(dist);

// GitHub Pages is case-sensitive; do not rely on Windows' case-insensitive fs.
const exactSet = new Set(allFiles.map((file) => path.relative(dist, file).replace(/\\/g, "/")));
const lowerSet = new Set([...exactSet].map((file) => file.toLowerCase()));

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
    let relative = decoded.replace(/^\/+/, "");
    let target;
    if (!relative) target = "index.html";
    else if (relative.endsWith("/")) target = `${relative}index.html`;
    else if (path.posix.extname(relative)) target = relative;
    else target = `${relative}/index.html`;

    // Public content URLs are lowercase. Assets and dynamic tag routes keep
    // their real case (`/tags/AI/`, `/_astro/page.cNngjUgL.js`).
    const targetLower = target.toLowerCase();
    const caseSensitive =
      target.startsWith("tags/") ||
      target.startsWith("_astro/") ||
      target.startsWith("assets/") ||
      !target.endsWith("/index.html");
    if (caseSensitive) {
      if (exactSet.has(target)) continue;
    } else if (target === targetLower && lowerSet.has(targetLower)) {
      continue;
    }
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
