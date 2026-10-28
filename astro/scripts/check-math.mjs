import fs from "node:fs";
import path from "node:path";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeKatex from "rehype-katex";
import { visit } from "unist-util-visit";

const macros = {
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
};

const processor = unified()
  .use(remarkParse)
  .use(remarkMath)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeKatex, { throwOnError: true, macros });

const root = path.resolve("src", "content", "docs");
const files = [];
function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (name === "_archive" || name === "node_modules" || name === "i18n") continue;
      walk(full);
    } else if (name.endsWith(".md") || name.endsWith(".mdx")) {
      files.push(full);
    }
  }
}
walk(root);

let totalMath = 0;
const errors = [];
for (const file of files) {
  const raw = fs.readFileSync(file, "utf8");
  const body = raw.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "");
  let count = 0;
  try {
    const tree = processor.parse(body);
    visit(tree, ["math", "inlineMath"], () => {
      count += 1;
    });
    totalMath += count;
    await processor.run(tree);
  } catch (error) {
    errors.push({
      file: path.relative(root, file),
      message: error instanceof Error ? error.message.split("\n")[0] : String(error),
    });
  }
}

console.log(JSON.stringify({
  files: files.length,
  formulas: totalMath,
  errors: errors.length,
  sampleErrors: errors.slice(0, 25),
}, null, 2));
