var test = require("tape");
import { DocumentBodyDimensionsMonitor, monitor, embed } from "../index.js";
import { listenToSize } from "../wrapper.js";

test("can import from iframe code", function(test) {
  test.equal(typeof monitor, "function");
  test.equal(typeof embed, "function");
  test.equal(typeof DocumentBodyDimensionsMonitor, "function");
  test.end();
});

test("can import wrapper code", function(test) {
  test.equal(typeof listenToSize, "function");
  test.end();
});
