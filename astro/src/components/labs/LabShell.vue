<script setup>
defineProps({
  title: { type: String, required: true },
  formula: { type: String, default: "" },
  description: { type: String, default: "" },
});

defineEmits(["reset"]);
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
        <button class="lab__reset" type="button" @click="$emit('reset')">重置参数</button>
      </aside>
    </div>
  </section>
</template>
