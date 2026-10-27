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
console.log("HOME sidebar links:", await page.locator('nav a[href*="/YanYu-Site/"]').count());
await page.screenshot({ path: path.join(out, "phaseb-home.png") });

await page.locator(".lab-card").first().click();
await page.waitForTimeout(600);
console.log("CARD ->", page.url());

// Content page (sidebar groups are collapsed by default; navigate directly)
await page.goto(`${base}/maththeory/advanced-algebra/linear-space/g1-线性空间的定义与基本性质/讲义/`, { waitUntil: "networkidle" });
await page.waitForTimeout(700);
console.log("G1 URL:", page.url());
console.log("G1 title:", await page.title());
console.log("G1 katex:", await page.locator(".katex").count());
console.log("G1 asides:", await page.locator(".starlight-aside").count());
await page.screenshot({ path: path.join(out, "phaseb-g1.png") });

// Works and blog visual/content checks
await page.goto(`${base}/mathmodel/works/`, { waitUntil: "networkidle" });
console.log("WORKS title:", await page.title());
console.log("WORKS tables:", await page.locator("table").count());
await page.screenshot({ path: path.join(out, "phaseb-works.png") });

await page.goto(`${base}/blog/`, { waitUntil: "networkidle" });
console.log("BLOG title:", await page.title());
console.log("BLOG cards:", await page.locator(".card").count());
await page.screenshot({ path: path.join(out, "phaseb-blog.png") });

// Lab: two islands
requests.length = 0;
await page.goto(`${base}/maththeory/analytic-geometry/lab/`, { waitUntil: "networkidle" });
await page.waitForTimeout(1200);
console.log("LAB canvases:", await page.locator("canvas").count());
const labChunks = [...new Set(requests.filter((u) => u.includes("/_astro/") && u.endsWith(".js")))].map((u) => u.split("/").pop());
console.log("LAB JS chunks:", JSON.stringify(labChunks));
await page.screenshot({ path: path.join(out, "phaseb-lab.png") });
await page.locator(".lab__tabs button", { hasText: "单叶双曲面" }).click();
await page.waitForTimeout(400);
await page.screenshot({ path: path.join(out, "phaseb-lab-hyperboloid.png") });

// Search full index
await page.goto(`${base}/`, { waitUntil: "networkidle" });
const searchButton = page.locator("button[data-open-modal], site-search button, button[aria-label*='Search'], button[aria-label*='搜索']").first();
if (await searchButton.count()) {
  await searchButton.click();
  await page.waitForTimeout(500);
  const input = page.locator("input[type='search'], input[type='text']").first();
  await input.fill("线性空间");
  await page.waitForTimeout(1500);
  console.log("SEARCH:", (await page.locator("body").innerText()).match(/\d+ results? for [^\n]+/)?.[0] || "no count");
  await page.screenshot({ path: path.join(out, "phaseb-search.png") });
}

// Old uppercase URL should still be reachable
await page.goto(`${base}/mathmodel/works/01_51MCM-2026/`, { waitUntil: "networkidle" });
console.log("OLD URL title:", await page.title());
console.log("OLD URL 200:", await page.locator("h1").count());

// Mobile
const mobile = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
await mobile.goto(`${base}/maththeory/analytic-geometry/lab/`, { waitUntil: "networkidle" });
await mobile.waitForTimeout(1000);
console.log("MOBILE canvases:", await mobile.locator("canvas").count());
await mobile.screenshot({ path: path.join(out, "phaseb-mobile.png") });

console.log("CONSOLE ERRORS:", JSON.stringify(consoleErrors.slice(0, 10)));
console.log("PAGE ERRORS:", JSON.stringify(pageErrors.slice(0, 10)));
await browser.close();
