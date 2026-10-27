# Phase C Report：实验平台与实验迁移

- 日期：2026-10-27
- 范围：把解析几何实验台升级为可复用的 lab 平台，并迁移/新增实验
- 结论：**Phase C 完成**；剩余 Phase D（首页/标签/redirect 优化/切换）

---

## 1. 架构

新增：

- `src/components/labs/LabShell.vue`：统一实验布局（标题、公式、描述、stage、controls）；
- `src/components/labs/LabExplorer.vue`：实验平台外壳（标签、异步 lab、hash deep link）；
- `src/data/labs.json`：实验注册表（slug / title / formula / description / component / status）；
- `src/lib/labs.ts`：Zod 校验注册表；
- `src/components/labs/`：
  - `VectorLab.vue`
  - `LinePlaneLab.vue`
  - `ConicLab.vue`
  - `QuadricLab.vue`
  - `ParametricLab.vue`
  - `TransformLab.vue`

所有 lab 复用 `LabShell`；`LabExplorer` 用 `defineAsyncComponent` 按标签懒加载，
每个实验独立 chunk；hash 支持 `#vector` / `#quadric` / `#transform` 等深链。

---

## 2. 实验清单

| slug | 实验 | 维度 | 主要交互 | 对应模块 |
|---|---|---|---|---|
| `vector` | 向量与度量 | 3D | 长度、夹角、点积/叉积读数 | A2 |
| `line-plane` | 直线与平面 | 3D | 法向倾角/方位、直线方向、线面角 | B1 |
| `conic` | 圆锥曲线 | 2D | 离心率、半通径、焦点/准线 | B2 |
| `quadric` | 二次曲面 | 3D | 椭球/单叶双曲面/马鞍面、尺度 | B3 |
| `parametric` | 参数曲面 | 3D | 环面/莫比乌斯环、R/r | B4 |
| `transform` | 线性变换 | 2D | 2×2 矩阵、网格/单位圆/行列式 | C1 |

---

## 3. 代码分割与预算

| 产物 | raw | gzip |
|---|---:|---:|
| `OrbitControls`（Three.js + controls 共享 chunk） | 756,438 B | **188,711 B** |
| `QuadricLab` | 4,513 B | 2,509 B |
| `ParametricLab` | 4,473 B | ~2.5 KB |
| `LinePlaneLab` | 4,416 B | ~2.4 KB |
| `VectorLab` | 4,335 B | ~2.4 KB |
| `TransformLab` | 3,943 B | ~2.2 KB |
| `ConicLab` | 3,912 B | ~2.2 KB |
| `LabExplorer` | 3,780 B | 1,947 B |
| `LabShell` | 931 B | 521 B |

- 初始进入实验台只加载 `LabExplorer` + 当前实验（默认 Vector）+ 共享 Three chunk；
- 切换到二次曲面时才加载 `QuadricLab` chunk；
- 每个实验 2–4 KB raw，符合“每实验独立 chunk”的目标；
- Three 共享 chunk gzip 约 189 KB，低于单页 200 KB 预算。

---

## 4. 验证

| 项目 | 结果 |
|---|---|
| `astro build` | 88 页 / 5.26 s |
| `astro check` | 0 errors / 0 warnings / 0 hints |
| 内部链接 | 0 broken / 97 HTML |
| KaTeX | 2,951 个 / 0 error |
| Pagefind | 562.7 KB |
| 中文搜索 | “线性空间” 53 条 |
| 旧 sitemap URL | 87/87 200 |
| 新 sitemap URL | 87/87 200 |
| 浏览器 console/page error | 0 / 0 |
| Ubuntu Astro Check workflow | **success**（check/math/build/link/upload） |

Ubuntu artifact 约 **3.35 MB**，明显小于 Windows 本地的 23 MB；
这确认了本地“大小写 alias 重复页面”是 Windows 大小写不敏感文件系统造成的现象，
Linux 构建下 alias 是轻量 redirect。

浏览器已验证：

- 6 个实验标签全部切换成功，每个仅 1 个 canvas；
- 深链 `#transform` 正确选中“线性变换”；
- 首页 6 张实验卡片；
- 二次曲面子标签“单叶双曲面”正常；
- 移动端实验台正常；
- 旧作品 URL 正常。

截图检查：向量、直线与平面、参数曲面、线性变换、二次曲面均正常。

---

## 5. 已处理的 Phase B 遗留

- 实验台 URL 修正为 `/maththeory/analytic-geometry/lab/`；
- 实验台路由与注册表统一；
- 实验卡片 6 张由 `labs.json` 生成；
- 组件头部重复信息移除；
- 向量实验相机/坐标轴优化；
- Vite chunk warning 通过 800 KB 预算阈值消除（Three 共享 chunk gzip 189 KB）；
- 增加 Ubuntu Astro Check workflow（`.github/workflows/astro-check.yml`）。

> 本地 Windows 下大小写 alias 会落到同一物理路径，看起来像完整重复页面；
> 这是 Windows 大小写不敏感文件系统的表现。Ubuntu CI 已通过，artifact 约 3.35 MB，
> 说明 Linux 构建下 alias 是轻量 redirect；Phase D 再决定是否彻底移除本地 alias 目录。

---

## 6. 遗留到 Phase D

1. 完整首页移植（两栏 Hero + 3D 轮播）。
2. tags 聚合页。
3. Starlight 404 fallback warning（内置 404）。
4. GitHub Actions 切换 Astro 构建 / Pages 部署与回滚方案。
5. 实验 presets / reset / 参数 URL 编码等增强。
