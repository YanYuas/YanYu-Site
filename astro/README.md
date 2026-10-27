# Astro Spike

Phase A spike for the long-term Astro + Starlight + Vue migration.
**Not the production site.** Production is still the MkDocs site at the repository root.

## Commands

```bash
npm install
npm run dev      # http://localhost:4321/YanYu-Site/
npm run build    # dist/
npm run check    # astro check
npm run check:math
```

## What is in this spike

- Starlight docs shell, dark/gold theme override;
- custom splash home + data-driven lab cards (`src/data/labs.json` + Zod);
- G1 lecture migrated as a real math page;
- two Vue islands:
  - `QuadricLab.vue` — Three.js, ellipsoid / hyperboloid / saddle;
  - `ConicLab.vue` — Canvas 2D, conic focus-directrix;
- i18n collection (zh-CN);
- Pagefind search;
- base path `/YanYu-Site` handled; sidebar links are auto-prefixed by Starlight.

## Validation notes

- `npm run check`: 0 errors / 0 warnings.
- `npm run check:math`: all 87 Markdown files, 2,961 formulas, 0 KaTeX errors.
- Full trial (87 docs copied under `full/`): 93 pages built in ~16.6 s, 2,966 KaTeX renders, 0 errors.
- Pagefind: Chinese query “线性空间” returns 2 results.
- Browser (Playwright + system Chrome): home, G1, lab; 0 console errors; 3D + 2D canvases; mobile 390×844.
- Three.js island: 760,658 B raw / 190,933 B gzip; Conic island: 3,805 B / 1,947 B gzip.

## Known migration items

- 35 MkDocs `!!!` admonitions → Starlight `:::note[...]` (one G1 aside converted as proof).
- 6 Material grid cards → Astro/Vue components.
- Some pages lack frontmatter title; trial build auto-added titles.
- Filenames are lower-cased in routes (`G1.md` → `/g1/`); sidebar/links must use the generated slug.
- Custom two-column home/hero and full visual parity are not ported yet.
- Starlight warns about its built-in 404 fallback and large Three.js chunk; non-blocking.

## Local browser check

```bash
# terminal 1: serve dist under the base path
python -m http.server 4331 --bind 127.0.0.1 --directory <preview-root-with-YanYu-Site>

# terminal 2:
CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe" npm run check:browser
```

See [SPIKE_REPORT.md](./SPIKE_REPORT.md) for details.
