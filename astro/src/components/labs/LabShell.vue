<script setup>
import { ref } from "vue";

defineProps({
  title: { type: String, required: true },
  formula: { type: String, default: "" },
  description: { type: String, default: "" },
});

defineEmits(["reset"]);

const copied = ref(false);
const copyFailed = ref(false);
let timer;

async function copyLink() {
  try {
    await navigator.clipboard.writeText(window.location.href);
    copied.value = true;
    copyFailed.value = false;
  } catch {
    copied.value = false;
    copyFailed.value = true;
  }
  clearTimeout(timer);
  timer = window.setTimeout(() => {
    copied.value = false;
    copyFailed.value = false;
  }, 1800);
}
</script>

<template>
  <section class="lab-shell">
    <header class="lab-shell__head">
      <div class="lab-shell__title">
        <strong>{{ title }}</strong>
        <code v-if="formula">{{ formula }}</code>
      </div>
      <p v-if="description" class="lab-shell__desc">{{ description }}</p>
    </header>
    <div class="lab">
      <div class="lab__stage">
        <slot name="stage" />
      </div>
      <aside class="lab__panel">
        <slot name="controls" />
        <div class="lab__actions" role="group" aria-label="实验操作">
          <button class="lab__reset" type="button" @click="$emit('reset')">重置参数</button>
          <button class="lab__share" type="button" @click="copyLink">
            {{ copied ? "已复制" : copyFailed ? "复制失败" : "复制参数链接" }}
          </button>
        </div>
        <p class="sr-only" role="status" aria-live="polite">
          {{ copied ? "参数链接已复制" : copyFailed ? "复制失败，请手动复制地址栏链接" : "" }}
        </p>
      </aside>
    </div>
  </section>
</template>
