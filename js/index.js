const MONITOR_INTERVAL = 1000;

class DocumentBodyDimensionsMonitor {
  constructor(iframeId) {
    this.iframeId = iframeId;
    this.lastWidth = -1;
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
    const width = document.body.parentElement.clientWidth;
    const height = document.body.parentElement.clientHeight;
    if (width !== this.lastWidth || height !== this.lastHeight) {
      this.lastWidth = width;
      this.lastHeight = height;
      this.report();
    }
  }

  report() {
    window.parent.postMessage(
      {
        type: "iframeSize",
        width: this.lastWidth,
        height: this.lastHeight,
        iframeId: this.iframeId
      },
      "*"
    );
  }
}

export const monitor = iframeId => {
  new DocumentBodyDimensionsMonitor(iframeId).start();
};
