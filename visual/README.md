# P2 · 视觉实验室（原型）

这个目录是「视觉升级（P2）」的技术原型，**不参与 MkDocs 构建**，也不会上线。
它用来验证三件事：

1. Three.js 在这台机器/这个站点上是否跑得动；
2. 数学曲面（二次型）作为交互内容的观感；
3. 用 Vite 打包后，体积、降级和接入方式是否可控。

## 跑起来

### 方式一：不构建，直接看（推荐在受限环境里用）

```bash
cd visual
npm install
cd ..
python -m http.server 8080 --directory visual
```

然后打开 http://127.0.0.1:8080/ 。
这个方式用浏览器原生 `importmap` 直接加载 `node_modules` 里的 three，
不需要 Vite，也不需要打包。

### 方式二：Vite 开发/构建（在普通本机或 CI 里用）

```bash
cd visual
npm install
npm run dev      # 开发预览
npm run build    # 产物在 visual/dist/（已 gitignore）
```

> 注意：当前 DSH 沙箱禁止子进程管道，Vite 8 在沙箱里构建会报 `spawn EPERM`；
> 在普通 Windows/macOS/CI 环境里正常。原型本身已经用 importmap 方式验证了源码结构。

## 当前内容

- 三种二次型曲面：椭球面、单叶双曲面、双曲抛物面
- OrbitControls：拖动旋转、滚轮缩放
- `prefers-reduced-motion` 时关闭自动旋转
- 无 WebGL 时显示静态说明（不会 blank）
- 金色线框 + 半透明实体，和站点现有的深蓝/金色视觉语言一致

## 接入站点的计划（尚未执行）

1. **先定页面**：优先放「高等代数 → G7 二次型与曲面」，作为讲义里的交互附录；
   首页 hero 的 3D 是第二个候选，不是第一优先。
2. **构建方式**：Vite 打包成单个 JS（three 按需 tree-shake），
   产物放 `docs/javascripts/visual/`；或者干脆在 CI 里加 Node 构建步骤。
3. **加载策略**：首屏不加载；进入页面/点击「打开交互」后再 `import()`。
4. **预算**：gzip 后 JS < 300 KB；移动端默认不自动初始化，给按钮手动开启。
5. **降级**：WebGL 不可用、`prefers-reduced-motion`、低端设备 → 静态 SVG/说明。
6. **验收**：`prefers-reduced-motion`、键盘操作、退出页面时 `dispose()`、
   Lighthouse 移动端性能不低于当前基线。

## 为什么不直接改 MkDocs 页面

- 需要先确认视觉方向、交互粒度和性能预算，避免把原型代码直接塞进内容页；
- 原型目录可以随时删除，不影响线上站点；
- 确认后再做「Vite 构建 + MkDocs 引用」的正式接入。

## 技术栈

- [Three.js](https://threejs.org/) 0.186.x
- [Vite](https://vite.dev/) 8.x
- 原生 CSS，无 UI 框架
