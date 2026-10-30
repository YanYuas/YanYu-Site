import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { docsLoader } from "@astrojs/starlight/loaders";
import { docsSchema, i18nSchema } from "@astrojs/starlight/schema";
import { glob } from "astro/loaders";

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      extend: z.object({
        tags: z.array(z.string()).optional(),
      }),
    }),
  }),
  i18n: defineCollection({
    loader: glob({ pattern: "**/*.json", base: "./src/content/i18n" }),
    schema: i18nSchema(),
  }),
};
