const MONITOR_INTERVAL = 200;

export class DocumentBodyDimensionsMutationObserverMonitor {
  constructor() {
    this.lastHeight = -1;

    this.onMutation = entries => {
      const height = document.body.clientHeight;
      if (height !== this.lastHeight) {
        this.lastHeight = height;
        postHeight(this.lastHeight);
      }
    };
  }

  start() {
    this.observer = new MutationObserver(this.onMutation);
    this.observer.observe(document.body, {
      childList: true,
      attributes: true,
      subtree: true
    });
  }
}

export class DocumentBodyDimensionsResizeObserverMonitor {
  constructor() {
    if (typeof window.ResizeObserver === "undefined") {
      throw Error("ResizeObserver is not supported");
    }
    this.lastHeight = -1;

    this.onResize = entries => {
      for (let entry of entries) {
        const height = entry.contentRect.height;
        if (height !== this.lastHeight) {
          this.lastHeight = height;
          postHeight(this.lastHeight);
        }
      }
    };
  }

  start() {
    this.observer = new ResizeObserver(this.onResize);
    this.observer.observe(document.body);
  }
}

export class DocumentBodyDimensionsPollingMonitor {
  constructor() {
    this.lastHeight = -1;
    this.timer = undefined;

    this.checkAndSchedule = () => {
      if (!this.monitoring) return;
      this.check();
      this.monitoring = setTimeout(this.checkAndSchedule, MONITOR_INTERVAL);
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
      postHeight(this.lastHeight);
    }
  }
}

function postHeight(height) {
  window.parent.postMessage(
    {
      type: "iframeSize",
      height
    },
    "*"
  );
}

export const monitor = () => {
  if (typeof window.ResizeObserver !== "undefined") {
    new DocumentBodyDimensionsResizeObserverMonitor().start();
  } else {
    new DocumentBodyDimensionsMutationObserverMonitor().start();
  }
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
