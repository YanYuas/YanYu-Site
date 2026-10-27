import resolve from "@rollup/plugin-node-resolve";
import terser from "@rollup/plugin-terser";

export default {
  input: "src/hero3d.js",
  output: {
    file: "../docs/javascripts/vendor/hero-3d.bundle.js",
    format: "es",
    sourcemap: false,
  },
  plugins: [
    resolve(),
    terser({
      format: { comments: false },
      compress: { passes: 2 },
      mangle: true,
    }),
  ],
};
