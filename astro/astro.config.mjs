import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import vue from "@astrojs/vue";
import { unified } from "@astrojs/markdown-remark";
import remarkMath from "remark-math";
import { visit } from "unist-util-visit";
import rehypeKatex from "rehype-katex";
import sidebar from "./src/data/sidebar.generated.mjs";
import redirects from "./src/data/redirects.generated.mjs";

const katexOptions = {
  // 与现有 MathJax 配置对齐的常用宏
  macros: {
    "\\R": "\\mathbb{R}",
    "\\N": "\\mathbb{N}",
    "\\Z": "\\mathbb{Z}",
    "\\Q": "\\mathbb{Q}",
    "\\C": "\\mathbb{C}",
    "\\dim": "\\operatorname{dim}",
    "\\rank": "\\operatorname{rank}",
    "\\ker": "\\operatorname{ker}",
    "\\im": "\\operatorname{im}",
    "\\tr": "\\operatorname{tr}",
    "\\det": "\\operatorname{det}",
    "\\abs": "\\left|#1\\right|",
    "\\norm": "\\left\\|#1\\right\\|",
    "\\iff": "\\Longleftrightarrow",
    "\\implies": "\\Longrightarrow",
    "\\empty": "\\varnothing",
  },
  throwOnError: false,
  strict: false,
  output: "html",
};

const katexTransformer = rehypeKatex(katexOptions);

// 体量最大的两套讲义改为浏览器端 KaTeX：服务端只输出原始 $...$。
// 这样 HTML 从上百 MB 降到可部署体积，同时保留 KaTeX 的排版。
function selectiveKatex() {
  return (tree, file) => {
    const path = String(file.path ?? file.history?.[0] ?? "").replaceAll("\\", "/");
    if (path.includes("/maththeory/analytic-geometry/notes/")) return;
    return katexTransformer(tree, file);
  };
}

// remark-math 节点如果直接跳过 rehype-katex，会被 mdast→hast 丢掉。
// 这里先把它们变成带原始 TeX 的 span/div，交给浏览器端 KaTeX 渲染。
function clientMath() {
  return (tree, file) => {
    const path = String(file.path ?? file.history?.[0] ?? "").replaceAll("\\", "/");
    if (!path.includes("/maththeory/analytic-geometry/notes/")) return;

    const escapeHtml = (value) =>
      value
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;");

    visit(tree, "inlineMath", (node, index, parent) => {
      if (!parent || index === undefined) return;
      parent.children[index] = {
        type: "html",
        value: `<span class="math math-inline">${escapeHtml(node.value)}</span>`,
      };
    });

    visit(tree, "math", (node, index, parent) => {
      if (!parent || index === undefined) return;
      parent.children[index] = {
        type: "html",
        value: `<div class="math math-display">${escapeHtml(node.value)}</div>`,
      };
    });
  };
}

const markdownProcessor = unified({
  remarkPlugins: [remarkMath, clientMath],
  rehypePlugins: [selectiveKatex],
});

export default defineConfig({
  site: "https://YanYuas.github.io",
  base: "/YanYu-Site",
  trailingSlash: "always",
  build: {
    format: "directory",
  },
  vite: {
    build: {
      // Three.js + OrbitControls 共享 chunk 约 756 KB raw / 191 KB gzip。
      chunkSizeWarningLimit: 800,
    },
  },
  redirects,
  markdown: {
    processor: markdownProcessor,
  },
  integrations: [
    starlight({
      title: "衍煜 · YanYuas",
      description: "数学与应用数学本科生 · 数学理论、解析几何与随笔",
      favicon: "/assets/images/favicon.svg",
      customCss: ["./src/styles/custom.css"],
      head: [
        {
          tag: "script",
          content:
            "try{if(!localStorage.getItem('starlight-theme'))localStorage.setItem('starlight-theme','light')}catch(e){}",
        },
        {
          tag: "script",
          content:
            "(()=>{const set=()=>{const n=document.querySelectorAll('.pagefind-ui__search-input');n.forEach(i=>{if(!i.getAttribute('aria-label'))i.setAttribute('aria-label','站内搜索')});if(n.length)o.disconnect()};const o=new MutationObserver(set);o.observe(document.documentElement,{childList:true,subtree:true});set()})()",
        },
        {
          tag: "meta",
          attrs: {
            property: "og:image",
            content: "https://yanyuas.github.io/YanYu-Site/assets/images/og-default.webp",
          },
        },
        {
          tag: "meta",
          attrs: { property: "og:image:width", content: "1200" },
        },
        {
          tag: "meta",
          attrs: { property: "og:image:height", content: "630" },
        },
        {
          tag: "meta",
          attrs: {
            property: "og:image:alt",
            content: "水火与光之间的衍煜",
          },
        },
        {
          tag: "meta",
          attrs: {
            name: "twitter:image",
            content: "https://yanyuas.github.io/YanYu-Site/assets/images/og-default.webp",
          },
        },
      ],
      components: {
        Hero: "./src/components/home/HomeHero.astro",
        MarkdownContent: "./src/components/content/MarkdownContent.astro",
      },
      social: [
        { icon: "github", label: "GitHub", href: "https://github.com/YanYuas" },
      ],
      locales: {
        root: { label: "简体中文", lang: "zh-CN" },
      },
      sidebar,
    }),
    vue(),
  ],
});
