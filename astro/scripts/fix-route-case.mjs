// Canonical public URLs are lowercase on GitHub Pages. The Windows build may
// keep old uppercase directory names, so compare case-insensitively and always
// write the lowercase route. This is a one-time repair after migration.
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const dist = path.join(root, "dist");
const base = "/YanYu-Site";

const htmlFiles = [];
function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) walk(full);
    else if (name.endsWith(".html")) htmlFiles.push(full);
  }
}
walk(dist);

const routes = [];
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  // Skip generated redirect pages: their paths are aliases, not canonical routes.
  if (/http-equiv=["']refresh["']/i.test(html)) continue;
  const rel = path.relative(dist, file).replace(/\\/g, "/");
  if (rel === "index.html") routes.push("/");
  else if (rel.endsWith("/index.html")) routes.push(`/${rel.slice(0, -"index.html".length)}`);
  else routes.push(`/${rel}`);
}

const exact = new Set(routes.map((route) => route.toLowerCase()));
const lower = new Map(routes.map((route) => [route.toLowerCase(), route.toLowerCase()]));
let unresolved = 0;

function canonical(route) {
  const withoutSuffix = route.split("#")[0].split("?")[0];
  const lowerRoute = withoutSuffix.toLowerCase();
  if (exact.has(lowerRoute)) return lower.get(lowerRoute) + route.slice(withoutSuffix.length);
  unresolved += 1;
  return route;
}

// 1. Sidebar links.
const sidebarPath = path.join(root, "src/data/sidebar.generated.mjs");
let sidebarChanges = 0;
let sidebar = fs.readFileSync(sidebarPath, "utf8");
sidebar = sidebar.replace(/("link":\s*")([^"]+)(")/g, (_whole, before, link, after) => {
  if (!link.startsWith("/")) return _whole;
  const next = canonical(link);
  if (next !== link) sidebarChanges += 1;
  return `${before}${next}${after}`;
});
fs.writeFileSync(sidebarPath, sidebar);

// 2. Redirect targets.
const redirectsPath = path.join(root, "src/data/redirects.generated.mjs");
let redirectChanges = 0;
let redirects = fs.readFileSync(redirectsPath, "utf8");
redirects = redirects.replace(/(":\s*")(\/YanYu-Site[^"]*)(")/g, (_whole, before, target, after) => {
  const route = target.slice(base.length) || "/";
  const nextRoute = canonical(route);
  const next = `${base}${nextRoute}`;
  if (next !== target) redirectChanges += 1;
  return `${before}${next}${after}`;
});
fs.writeFileSync(redirectsPath, redirects);

// 3. Absolute internal links inside Markdown/MDX.
let contentChanges = 0;
function walkContent(dir) {
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) walkContent(full);
    else if (name.endsWith(".md") || name.endsWith(".mdx")) {
      const before = fs.readFileSync(full, "utf8");
      const after = before.replace(/\]\((\/YanYu-Site\/[^)\s#?]+)([^)]*)\)/g, (_whole, target, suffix) => {
        const route = target.slice(base.length) || "/";
        const nextRoute = canonical(route);
        const next = `${base}${nextRoute}`;
        if (next !== target) contentChanges += 1;
        return `](${next}${suffix})`;
      });
      if (after !== before) fs.writeFileSync(full, after);
    }
  }
}
walkContent(path.join(root, "src/content/docs"));

console.log(
  JSON.stringify(
    { routes: routes.length, sidebarChanges, redirectChanges, contentChanges, unresolved },
    null,
    2
  )
);
