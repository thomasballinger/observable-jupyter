const MONITOR_INTERVAL = 1000;

class DocumentBodyDimensionsMonitor {
  constructor(iframeId) {
    this.iframeId = iframeId;
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
      this.report();
    }
  }

  report() {
    window.parent.postMessage(
      {
        type: "iframeSize",
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
