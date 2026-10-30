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

function onTabKeydown(event) {
  const keys = ["ArrowRight", "ArrowLeft", "Home", "End"];
  if (!keys.includes(event.key)) return;
  const tabs = Array.from(
    event.currentTarget.closest('[role="tablist"]')?.querySelectorAll('[role="tab"]') ?? []
  );
  const index = tabs.indexOf(event.currentTarget);
  if (index === -1) return;
  event.preventDefault();
  const next =
    event.key === "Home"
      ? 0
      : event.key === "End"
        ? tabs.length - 1
        : event.key === "ArrowRight"
          ? (index + 1) % tabs.length
          : (index - 1 + tabs.length) % tabs.length;
  const lab = labs[next];
  if (!lab) return;
  select(lab.slug);
  tabs[next]?.focus();
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
        :id="`lab-tab-${lab.slug}`"
        :key="lab.slug"
        :class="{ 'is-active': active === lab.slug }"
        role="tab"
        :aria-selected="active === lab.slug"
        :aria-controls="`lab-panel-${lab.slug}`"
        :tabindex="active === lab.slug ? 0 : -1"
        @click="select(lab.slug)"
        @keydown="onTabKeydown"
      >
        {{ lab.title }}
      </button>
    </nav>

    <div
      class="lab-explorer__panel"
      role="tabpanel"
      :id="`lab-panel-${current.slug}`"
      :aria-labelledby="`lab-tab-${current.slug}`"
      tabindex="0"
    >
      <Suspense>
        <component :is="currentComponent" :key="current.slug" />
        <template #fallback>
          <p class="lab-explorer__loading">正在加载实验…</p>
        </template>
      </Suspense>
    </div>
  </div>
</template>
