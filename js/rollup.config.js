import resolve from "@rollup/plugin-node-resolve";

export default [
  {
    input: "index.js",
    output: {
      file: "../observable_jupyter/iframe_bundle.js",
      format: "iife",
      name: "ObservableJupyterIframe"
    },
    plugins: [resolve()]
  },
  {
    input: "./wrapper.js",
    output: {
      file: "../observable_jupyter/wrapper_bundle.js",
      format: "iife",
      name: "ObservableJupyterWrapper"
    },
    plugins: [resolve()]
  }
];
