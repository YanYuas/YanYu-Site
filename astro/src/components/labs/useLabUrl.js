import { onBeforeUnmount, onMounted, watch } from "vue";

/**
 * Keep simple lab controls in the URL query string.
 * Example: /lab/?a=1.6&b=1.3&angle=55#vector
 */
export function useLabUrl(refs) {
  let ready = false;
  let applying = false;

  function readFromUrl() {
    applying = true;
    const params = new URLSearchParams(window.location.search);
    for (const [key, ref] of Object.entries(refs)) {
      if (!params.has(key)) continue;
      const raw = params.get(key);
      if (raw === null) continue;
      if (typeof ref.value === "number") {
        const value = Number(raw);
        if (Number.isFinite(value)) ref.value = value;
      } else {
        ref.value = raw;
      }
    }
    applying = false;
  }

  function writeToUrl(values) {
    if (!ready || applying) return;
    const params = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(values)) {
      if (value === null || value === undefined || value === "") params.delete(key);
      else params.set(key, String(value));
    }
    const query = params.toString();
    const next = `${window.location.pathname}${query ? `?${query}` : ""}${window.location.hash}`;
    window.history.replaceState(null, "", next);
  }

  const onPopState = () => readFromUrl();

  onMounted(() => {
    readFromUrl();
    ready = true;
    window.addEventListener("popstate", onPopState);
  });

  onBeforeUnmount(() => window.removeEventListener("popstate", onPopState));

  watch(
    () => Object.fromEntries(Object.entries(refs).map(([key, ref]) => [key, ref.value])),
    (values) => writeToUrl(values),
    { deep: true }
  );
}
