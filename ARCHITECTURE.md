written as I try to remind myself of how this works...

This is a Python package called observable_jupyter that exports one important method:

```
from observable_jupyter import embed
```

This `embed()` function calls the IPython [display](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.display) and [HTML](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.HTML) functions to inject some HTML and JavaScript code into a cell.

This HTML and some of this JavaScript is defined inline in the embed() function in [jupyter/jupyter_embed.py](./jupyter/jupyter_embed.py). Most of the JavaScript comes from [wrapper.js](./js/wrapper.js). This code defines attribution on hover of the Observable logo in the bottom right. It also creates an iframe and sets the `.srcdoc` property of the iframe to an HTML document (also defined inline in `embed()`) which includes JavaScript defined in [js/iframe_bundle.js](./js/wrapper.js). This JavaScript is a bit more substantial: it includes the requested notebook code and some [open source Observable runtime libraries]() imported by the  required to run a notebook.

Because this notebook code is requested from observablehq.com when the embed function is run, just viewing a notebook with this output does not require an internet connection. However executing the cell always does: the code is re-requested from observablehq each time.
