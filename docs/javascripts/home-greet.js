/* ==================================================================
   home-greet.js · 按时间变化的问候语
   ------------------------------------------------------------------
   灵感来自 lvy010 首页的 "Good Night I'm lvy, Nice to meet you!"
   首页 #greet 元素会在每天不同时段自动切换问候语，让站点有生命感。
   无依赖；找不到 #greet 元素时静默退出。
   ================================================================== */

(function () {
  function greet() {
    var h = new Date().getHours();
    if (h >= 5 && h < 11) return "早上好";
    if (h >= 11 && h < 13) return "中午好";
    if (h >= 13 && h < 18) return "下午好";
    if (h >= 18 && h < 23) return "晚上好";
    return "夜深了";
  }

  function apply() {
    var el = document.getElementById("greet");
    if (el) el.textContent = greet() + "，我是";
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", apply);
  } else {
    apply();
  }
})();
