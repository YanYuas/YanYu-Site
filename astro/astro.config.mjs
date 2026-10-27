import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import vue from "@astrojs/vue";
import { unified } from "@astrojs/markdown-remark";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

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
  markdown: {
    processor: markdownProcessor,
  },
  integrations: [
    starlight({
      title: "衍煜 · YanYuas",
      description: "数学与应用数学本科生 · 数学理论、解析几何与随笔",
      favicon: "/assets/images/favicon.svg",
      customCss: ["./src/styles/custom.css"],
      social: [
        { icon: "github", label: "GitHub", href: "https://github.com/YanYuas" },
      ],
      locales: {
        root: { label: "简体中文", lang: "zh-CN" },
      },
      sidebar: [
        { label: "首页", link: "/" },
        {
          label: "数学理论",
          items: [
            { label: "板块导览", link: "/maththeory/" },
            {
              label: "高等代数",
              items: [
                {
                  label: "G1 · 线性空间与子空间",
                  link: "/maththeory/advanced-algebra/linear-space/g1/",
                },
              ],
            },
            {
              label: "解析几何",
              items: [
                { label: "总览", link: "/analytic-geometry/" },
                { label: "交互实验台", link: "/analytic-geometry/lab/" },
              ],
            },
          ],
        },
      ],
    }),
    vue(),
  ],
});
