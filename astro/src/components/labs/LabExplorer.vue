<script setup>
import { computed, defineAsyncComponent, onMounted, onBeforeUnmount, ref } from "vue";
import labs from "../../data/labs.json";

const components = {
  VectorLab: defineAsyncComponent(() => import("./VectorLab.vue")),
  LinePlaneLab: defineAsyncComponent(() => import("./LinePlaneLab.vue")),
  ConicLab: defineAsyncComponent(() => import("./ConicLab.vue")),
  QuadricLab: defineAsyncComponent(() => import("./QuadricLab.vue")),
  ParametricLab: defineAsyncComponent(() => import("./ParametricLab.vue")),
  TransformLab: defineAsyncComponent(() => import("./TransformLab.vue")),
};

const active = ref(labs[0].slug);
const current = computed(() => labs.find((lab) => lab.slug === active.value) || labs[0]);
const currentComponent = computed(() => components[current.value.component]);

function select(slug) {
  active.value = slug;
  if (typeof window !== "undefined") {
    window.history.replaceState(null, "", `#${slug}`);
  }
}

function syncFromHash() {
  const slug = window.location.hash.replace(/^#/, "");
  if (slug && labs.some((lab) => lab.slug === slug)) active.value = slug;
}

onMounted(() => {
  syncFromHash();
  window.addEventListener("hashchange", syncFromHash);
});
onBeforeUnmount(() => window.removeEventListener("hashchange", syncFromHash));
</script>

<template>
  <div class="lab-explorer">
    <nav class="lab-explorer__tabs" role="tablist" aria-label="实验列表">
      <button
        v-for="lab in labs"
        :key="lab.slug"
        :class="{ 'is-active': active === lab.slug }"
        role="tab"
        :aria-selected="active === lab.slug"
        @click="select(lab.slug)"
      >
        {{ lab.title }}
      </button>
    </nav>

    <Suspense>
      <component :is="currentComponent" :key="current.slug" />
      <template #fallback>
        <p class="lab-explorer__loading">正在加载实验…</p>
      </template>
    </Suspense>
  </div>
</template>
