import { defineConfig } from "vite";

// 这个原型只负责“三维数学视觉”，不参与 MkDocs 构建。
// base: "./" 让构建产物可以直接用 file:// 或任意子路径打开。
export default defineConfig({
  base: "./",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    target: "es2020",
  },
});
