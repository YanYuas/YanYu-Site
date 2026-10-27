import { chromium } from "playwright-core";
import path from "node:path";

const chrome = process.env.CHROME_PATH || "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const out = process.env.TEMP || ".";
const base = process.env.SPIKE_BASE || "http://127.0.0.1:4331/YanYu-Site";

const browser = await chromium.launch({
  headless: true,
  executablePath: chrome,
  args: ["--no-sandbox", "--disable-dev-shm-usage", "--enable-unsafe-swiftshader"],
});

const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const consoleErrors = [];
const pageErrors = [];
const requests = [];
page.on("console", (msg) => {
  if (msg.type() === "error") consoleErrors.push(msg.text());
});
page.on("pageerror", (err) => pageErrors.push(String(err)));
page.on("request", (req) => requests.push(req.url()));

await page.goto(`${base}/`, { waitUntil: "networkidle" });
console.log("HOME title:", await page.title());
console.log("HOME h1:", await page.locator("h1").first().innerText());
console.log("HOME cards:", await page.locator(".lab-card").count());
console.log("HOME base links:", await page.locator('a[href*="/YanYu-Site/"]').count());
await page.screenshot({ path: path.join(out, "astro-home.png") });

// data-driven card -> lab anchor
await page.locator(".lab-card").first().click();
await page.waitForTimeout(500);
console.log("CARD ->", page.url());

// Sidebar link -> G1 content page, base path + lowercase route
// 首页是 splash，Starlight 不渲染侧边栏；从文档页进入。
await page.goto(`${base}/analytic-geometry/`, { waitUntil: "networkidle" });
await page.locator('a[href*="/maththeory/advanced-algebra/linear-space/g1/"]').first().click();
await page.waitForTimeout(700);
console.log("G1 URL:", page.url());
console.log("G1 title:", await page.title());
console.log("G1 katex:", await page.locator(".katex").count());
await page.screenshot({ path: path.join(out, "astro-g1.png") });

// Lab: two islands, separate chunks
requests.length = 0;
await page.goto(`${base}/analytic-geometry/lab/`, { waitUntil: "networkidle" });
await page.waitForTimeout(1200);
console.log("LAB canvases:", await page.locator("canvas").count());
console.log("LAB canvas sizes:", JSON.stringify(await page.locator("canvas").evaluateAll((els) =>
  els.map((el) => ({ w: el.width, h: el.height, cw: el.clientWidth, ch: el.clientHeight }))
)));
const labChunks = [...new Set(requests.filter((u) => u.includes("/_astro/") && u.endsWith(".js")))].map((u) => u.split("/").pop());
console.log("LAB JS chunks:", JSON.stringify(labChunks));
await page.screenshot({ path: path.join(out, "astro-lab.png") });
await page.locator(".lab__tabs button", { hasText: "单叶双曲面" }).click();
await page.waitForTimeout(400);
await page.screenshot({ path: path.join(out, "astro-lab-hyperboloid.png") });

// Search / Pagefind Chinese query
await page.goto(`${base}/`, { waitUntil: "networkidle" });
const searchButton = page.locator("button[data-open-modal], site-search button, button[aria-label*='Search'], button[aria-label*='搜索']").first();
if (await searchButton.count()) {
  await searchButton.click();
  await page.waitForTimeout(500);
  const input = page.locator("input[type='search'], input[type='text']").first();
  await input.fill("线性空间");
  await page.waitForTimeout(1200);
  console.log("SEARCH:", (await page.locator("body").innerText()).match(/\d+ results? for [^\n]+/)?.[0] || "no result count");
  await page.screenshot({ path: path.join(out, "astro-search.png") });
}

// Mobile
const mobile = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
await mobile.goto(`${base}/analytic-geometry/lab/`, { waitUntil: "networkidle" });
await mobile.waitForTimeout(1000);
console.log("MOBILE canvases:", await mobile.locator("canvas").count());
await mobile.screenshot({ path: path.join(out, "astro-lab-mobile.png") });

console.log("CONSOLE ERRORS:", JSON.stringify(consoleErrors.slice(0, 10)));
console.log("PAGE ERRORS:", JSON.stringify(pageErrors.slice(0, 10)));
await browser.close();
