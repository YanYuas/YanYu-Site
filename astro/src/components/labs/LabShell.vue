<script setup>
import { ref } from "vue";

defineProps({
  title: { type: String, required: true },
  formula: { type: String, default: "" },
  description: { type: String, default: "" },
});

defineEmits(["reset"]);

const copied = ref(false);
let timer;

async function copyLink() {
  try {
    await navigator.clipboard.writeText(window.location.href);
    copied.value = true;
    clearTimeout(timer);
    timer = window.setTimeout(() => {
      copied.value = false;
    }, 1800);
  } catch {
    copied.value = false;
  }
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
        <div class="lab__actions">
          <button class="lab__reset" type="button" @click="$emit('reset')">重置参数</button>
          <button class="lab__share" type="button" @click="copyLink">
            {{ copied ? "已复制" : "复制参数链接" }}
          </button>
        </div>
      </aside>
    </div>
  </section>
</template>
