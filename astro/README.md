# Astro Migration

Phase A spike + Phase B content migration + Phase C lab platform.
**Not the production site.** Production is still the MkDocs site at the repository root.

- Phase A report: [SPIKE_REPORT.md](./SPIKE_REPORT.md)
- Phase B report: [MIGRATION_REPORT.md](./MIGRATION_REPORT.md)
- Phase C report: [PHASE_C_REPORT.md](./PHASE_C_REPORT.md)

## Commands

```bash
npm install
npm run dev      # http://localhost:4321/YanYu-Site/
npm run build    # dist/
npm run check    # astro check
npm run check:math
npm run check:links
```

## What is in this migration

- Starlight docs shell, dark/gold theme override;
- custom splash home + data-driven lab cards (`src/data/labs.json` + Zod);
- all 85 migrated MkDocs content pages (custom home + lab kept separately);
- 6 interactive labs behind `LabExplorer.vue` + `labs.json` registry:
  - VectorLab / LinePlaneLab / ConicLab / QuadricLab / ParametricLab / TransformLab;
  - each lab is an async chunk; shared `LabShell.vue` layout;
  - hash deep links (`#vector`, `#quadric`, `#transform`, …).
- generated sidebar from `mkdocs.yml` nav (`src/data/sidebar.generated.mjs`);
- generated redirects (`src/data/redirects.generated.mjs`);
- i18n collection (zh-CN);
- Pagefind search;
- base path `/YanYu-Site` handled; Starlight prefixes sidebar links.

## Migration pipeline

```bash
..\.venv\Scripts\python.exe scripts\migrate-docs.py
npm run build
npm run check
npm run check:links
```

See [MIGRATION_REPORT.md](./MIGRATION_REPORT.md) for conversion stats and remaining items.
