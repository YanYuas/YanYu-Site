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
      ],
      components: {
        Hero: "./src/components/home/HomeHero.astro",
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
