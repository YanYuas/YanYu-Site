<script setup>
import { onBeforeUnmount, onMounted, ref } from "vue";

const canvas = ref(null);
const failed = ref(false);
let cleanup;

onMounted(() => {
  if (window.innerWidth <= 1000) return;
  if (!("WebGLRenderingContext" in window)) {
    failed.value = true;
    return;
  }
  const start = () => {
    import("./hero3d.js")
      .then(({ initHero3D }) => {
        cleanup = initHero3D(canvas.value);
        canvas.value?.parentElement?.classList.add("is-ready");
      })
      .catch((error) => {
        failed.value = true;
        console.warn("Hero 3D unavailable:", error);
      });
  };
  if ("requestIdleCallback" in window) requestIdleCallback(start, { timeout: 900 });
  else window.setTimeout(start, 300);
});

onBeforeUnmount(() => cleanup?.());
</script>

<template>
  <div class="hero-visual" :class="{ 'is-failed': failed }" aria-hidden="true">
    <canvas ref="canvas" id="hero-3d"></canvas>
    <div class="hero-visual__hud">
      <span class="hero-visual__no" id="hero-3d-no">01</span>
      <span class="hero-visual__name" id="hero-3d-name">椭球面</span>
      <span class="hero-visual__formula" id="hero-3d-formula">xᵀAx = 1</span>
    </div>
    <div class="hero-visual__dots" id="hero-3d-dots"></div>
  </div>
</template>
