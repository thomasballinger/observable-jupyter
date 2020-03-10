function getFrameByEvent(event) {
  return [...document.getElementsByTagName("iframe")].filter(iframe => {
    return iframe.contentWindow === event.source;
  })[0];
}

// Each embed gets its own event listener.
export function listenToSize(iframe) {
  function onMessage(msg) {
    if (!document.body.contains(iframe)) {
      // iframe is gone
      removeEventListener("message", onMessage);
    }
    const senderIframe = getFrameByEvent(msg);
    if (msg.data.type === "iframeSize" && senderIframe === iframe) {
      iframe.height = msg.data.height;
    }
  }

  window.addEventListener("message", onMessage);
}
