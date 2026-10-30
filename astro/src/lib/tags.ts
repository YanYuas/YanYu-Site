import { getCollection } from "astro:content";

export type TagPage = {
  title: string;
  description: string;
  section: string;
  href: string;
};

export type TagGroup = {
  tag: string;
  pages: TagPage[];
};

const sectionNames: Record<string, string> = {
  mathmodel: "数学建模",
  maththeory: "数学理论",
  blog: "随笔",
  journey: "成长",
  about: "关于",
};

/** Use the real file path: Astro content IDs can be lowercased, routes are not. */
function entryPath(entry: { id: string; filePath?: string }): string {
  const raw = entry.filePath ?? entry.id;
  const normalized = raw
    .replace(/\\/g, "/")
    .replace(/^.*?src\/content\/docs\//, "")
    .replace(/\.(md|mdx)$/, "")
    .replace(/(^|\/)index$/, "");
  return normalized ? `/${normalized.toLowerCase()}/` : "/";
}

function sectionName(id: string): string {
  return sectionNames[id.split("/")[0] ?? ""] ?? "站内";
}

/** All tags with the content pages that carry them. */
export async function getTagPages(): Promise<TagGroup[]> {
  const entries = await getCollection("docs");
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  const map = new Map<string, TagPage[]>();

  for (const entry of entries) {
    const tags = entry.data.tags ?? [];
    for (const raw of tags) {
      const tag = String(raw).trim();
      if (!tag) continue;
      const list = map.get(tag) ?? [];
      list.push({
        title: entry.data.title,
        description: entry.data.description ?? "",
        section: sectionName(entry.id),
        href: `${base}${entryPath(entry)}`,
      });
      map.set(tag, list);
    }
  }

  return [...map.entries()]
    .map(([tag, pages]) => ({
      tag,
      pages: pages.sort((a, b) => a.title.localeCompare(b.title, "zh-CN")),
    }))
    .sort((a, b) =>
      b.pages.length - a.pages.length || a.tag.localeCompare(b.tag, "zh-CN")
    );
}

/** URL-safe tag path, keeping the human-readable tag in the route. */
export function tagHref(tag: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  return `${base}/tags/${encodeURIComponent(tag)}/`;
}
