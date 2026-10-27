# P2 · 视觉实验室

这个目录是「视觉升级（P2）」的技术验证与源码目录。
**它不参与 MkDocs 构建**；但首页 hero 的正式三维包是从这里打包出去的。

## 当前状态

- ✅ 首页 hero：`src/hero3d.js` → 打包到 `docs/javascripts/vendor/hero-3d.bundle.js`，
  由 `docs/javascripts/home-3d.js` 在桌面端懒加载。
- 🧪 `visual/index.html` + `src/main.js`：独立的三种二次型曲面实验页（不发布）。
- ⏭️ 下一个接入点：高等代数 G7「二次型与曲面」的讲义附录。

## 跑独立实验页（不用构建）

```bash
cd visual
npm install
cd ..
python -m http.server 8080 --directory visual
```

打开 http://127.0.0.1:8080/ 。
用浏览器原生 `importmap` 直接加载 `node_modules` 里的 three，不需要 Vite。

## 重新打包首页 hero 3D

```bash
cd visual
npm install
npm run build:hero
```

输出：`docs/javascripts/vendor/hero-3d.bundle.js`（提交进仓库；CI 不需要 Node）。
当前产物：约 526 KB，gzip 后约 127 KB。

> `npm run build`（Vite）是独立实验页的构建方式；当前 DSH 沙箱禁止子进程管道，
> Vite 8 在沙箱里会报 `spawn EPERM`，普通本机/CI 正常。
> 首页 hero 用的是 Rollup 打包，已经在沙箱里验证通过。

## 首页 hero 的实现

- 形状：四种曲面交替展示，顺序为
  **椭球面 → 单叶双曲面 → 马鞍面 → 莫比乌斯环**，每种停留 8–9 秒，
  切换时 760ms 交叉淡入淡出 + 轻微缩放；不做顶点形变（拓扑不同，形变会穿模）
- HUD：底部显示 `01 / 椭球面 / xᵀAx = 1` 这样的编号、名称、公式，
  下方四段小横线表示当前轮次
- 加载：只在首页、桌面宽度（>1000px）、支持 WebGL 时，
  通过 `docs/javascripts/home-3d.js` 在空闲时间动态 `import()`
- 降级：手机/平板不加载；`prefers-reduced-motion` 只渲染第一帧静态画面；
  WebGL 失败时保留 CSS 金线装饰，不出现空白画布
- 主题：从 `--sa-gold` 读取颜色，深/浅模式自动变化
- 清理：暴露 `dispose()`，退出/重建时可释放几何体、材质、renderer

## 独立实验页的内容

- 三种二次型曲面：椭球面、单叶双曲面、双曲抛物面
- OrbitControls：拖动旋转、滚轮缩放
- `prefers-reduced-motion` 时关闭自动旋转
- 无 WebGL 时显示静态说明
- 金色线框 + 半透明实体，与站点视觉语言一致

## 下一步

1. 把同一套场景接到 G7 讲义，作为可交互附录（点击后再初始化）。
2. 增加「线性变换 / 特征向量」演示：矩阵参数由滑块控制。
3. 统一性能预算：hero gzip < 150 KB，单页交互 < 300 KB。
4. 如果交互内容继续变多，再评估是否迁 Astro/Starlight。

## 技术栈

- [Three.js](https://threejs.org/) 0.186.x
- [Vite](https://vite.dev/) 8.x（独立实验页）
- [Rollup](https://rollupjs.org/) 4.x（首页 hero 打包）
- 原生 CSS，无 UI 框架
