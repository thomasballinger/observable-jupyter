const MONITOR_INTERVAL = 1000;

export class DocumentBodyDimensionsMonitor {
  constructor(module) {
    this.lastHeight = -1;
    this.timer = undefined;
    this.module = module;

    this.checkAndSchedule = () => {
      if (!this.monitoring) return;
      this.check();
      this.monitoring = setTimeout(this.checkAndSchedule, MONITOR_INTERVAL);
    };

    this.onMessage = event => {
      if (window.parent !== event.source) {
        return;
      }
      if (msg.data.type === "cleanup") {
        this.cleanup();
      }
    };
  }

  start() {
    if (!this.monitoring) {
      this.monitoring = true;
      this.checkAndSchedule();
    }
  }

  stop() {
    if (this.monitoring) {
      clearTimeout(this.monitoring);
    }
    this.monitoring = undefined;
  }

  check() {
    const height = document.body.clientHeight;
    if (height !== this.lastHeight) {
      this.lastHeight = height;
      this.report();
    }
  }

  report() {
    window.parent.postMessage(
      {
        type: "iframeSize",
        height: this.lastHeight
      },
      "*"
    );
  }

  /* Never used in the normal iframe embedding since everything stops
   * when the iframe gets unmounted */
  cleanup() {
    this.stop();
    this.main.dispose();
  }
}

export const monitor = () => {
  new DocumentBodyDimensionsMonitor().start();
};

import { Runtime, Inspector } from "@observablehq/runtime";

export const embed = async (slug, into, cells, inputs = {}) => {
  const moduleUrl = "https://api.observablehq.com/" + slug + ".js?v=3";
  const define = (await import(moduleUrl)).default;
  const inspect = Inspector.into(into);
  const filter = cells ? name => cells.includes(name) : name => true;
  const main = new Runtime().module(define, name => filter(name) && inspect());
  for (let name of Object.keys(inputs)) {
    main.redefine(name, inputs[name]);
  }
  return main;
};
