import { z } from "astro/zod";
import raw from "../data/labs.json";

const LabSchema = z.object({
  slug: z.string().min(1),
  title: z.string().min(1),
  formula: z.string().min(1),
  description: z.string().min(1),
  status: z.enum(["spike", "beta", "stable"]),
});

export const labs = z.array(LabSchema).parse(raw);
