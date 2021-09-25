written as I try to remind myself of how this works...

This is a Python package called observable_jupyter that exports one important method:

```
from observable_jupyter import embed
```

This `embed()` function calls the IPython [display](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.display) and [HTML](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.HTML) functions to inject some HTML and JavaScript code into a cell.

This HTML and some of this JavaScript is defined inline in the embed() function in [jupyter/jupyter_embed.py](./jupyter/jupyter_embed.py). Most of the JavaScript comes from [wrapper.js](./js/wrapper.js) via the rollup bundle "wrapper_bundle.js." This code defines attribution on hover of the Observable logo in the bottom right.

This same injected HTML and JS in `embed()` also creates an iframe and sets the `.srcdoc` property of the iframe to an string which includes JavaScript defined in [js/index.js](./js/index.js) via the rollup bundle "iframe_bundle.js" This JavaScript is substantial, at about 100KB: it includes code that requests the notebook from observablehq.com and directly includes some [open source Observable runtime libraries](https://github.com/observablehq/runtime) required to run a notebook.

Because this notebook code is requested from observablehq.com when the embed function is run, just viewing a notebook with this output does not require an internet connection. However executing the cell always does: the code is re-requested from observablehq each time.

```
+Jupyter====================================+
|  cell 1                                   |
|  >>> from observable_jupyter import embed |
|  >>> 1 + 1                                |
| - - - - - - - - - - - - - - - - - - - - - |
|  cell 2 output                            |
|  2                                        |
|===========================================|
|  cell 2                                   |
|  >>> embed("@author/title")               |
| - - - - - - - - - - - - - - - - - - - - - |
|  cell 2 output                            |
|  +wrapper div-----------------------------+
|  | +iframe------------------------------+ |
|  | | <link rel="style" href=.../>       | |
|  | | <script> iframe_bundle.js </script>| |
|  | |  - runs notebook based on embed()  | |
|  | |  - monitors HTML body dimensions   | |
|  | |  - includes @observablehq/runtime  | |       +observablehq.com+
|  | |  - dynamically imports notebook    | |       |                |
|  | |    which may triggers many requests: |       |                |
|  | |    const define = (await import(x)).default  |                |
|  | |    request api.observablehq.com/@author/title.js?v=3----->    |
|  | |       <-----JavaScript module for notebook------------        |
|  | |    request api.observablehq.com/@mbostock/useful.js?v=3-->    |
|  | |       <-----JavaScript module for another notebook----        |
|  | |                                    | |       +----------------+
|  | |                                    | |          +npm or a CDN--+
|  | |    request cdn.jsdelivr.net/npm/d3@6---------------->          |
|  | |       <-------------JavaScript module of a dependency          |
|  | |    request cdn.jsdelivr.net/npm/moment-------------->          |
|  | |       <-------------JavaScript module of a dependency          |
|  | |                                    | |          |              |
|  | |                                    | |          +--------------+
|  | |                                    | |
|  | +------------------------------------+ |
|  |                                      | |
|  |     <span class="observable-logo">   | |
|  |       Edit @author/title on Observable |
|  |     </span>                          | |
|  |                                      | |
|  | <script>wrapper_bundle.js </script>  | |
|  |  - listens to size change msgs from iframe
|  |                                      | |
|  |                                      | |
|  +--------------------------------------+ |
+===========================================+
```
