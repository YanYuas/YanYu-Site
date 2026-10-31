import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import vue from "@astrojs/vue";
import { unified } from "@astrojs/markdown-remark";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import sidebar from "./src/data/sidebar.generated.mjs";
import redirects from "./src/data/redirects.generated.mjs";

const markdownProcessor = unified({
  remarkPlugins: [remarkMath],
  rehypePlugins: [
    [
      rehypeKatex,
      {
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
      },
    ],
  ],
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
