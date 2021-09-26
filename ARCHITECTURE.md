written as I try to remind myself of how this works...

This is a Python package called observable_jupyter that exports one important method:

```
from observable_jupyter import embed
```

This `embed()` function calls the IPython [display](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.display) and [HTML](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.HTML) functions to inject some HTML and JavaScript code into a cell.

This HTML and some of this JavaScript is defined inline in the embed() function in [jupyter/jupyter_embed.py](./jupyter/jupyter_embed.py). Some of this JavaScript comes from [wrapper.js](./js/wrapper.js) via the rollup bundle "wrapper_bundle.js," which creates the iframe (described below) that contains the running Observable notebook and the Observable logo in the bottom right that displays the author's name on hover.

The iframe created by that code has its `.srcdoc` property set to a string which includes JavaScript defined in [js/index.js](./js/index.js) via the rollup bundle "iframe_bundle.js" This JavaScript is substantial, at about 100KB: it includes code that requests the notebook from observablehq.com and directly includes some [open source Observable runtime libraries](https://github.com/observablehq/runtime) required to run a notebook.

Because this notebook code is requested from observablehq.com when the embed function is run, just viewing a notebook with this output does not require an internet connection. However executing the cell always does: the code is re-requested from observablehq each time.

```
+Jupyter in the users's web browser==========+
|In [1]: from observable_jupyter import embed|
|============================================|
|In [2]: 6 * 7                               |
|- - - - - - - - - - - - - - - - - - - - - - |
|Out[2]: 42                                  |
|============================================|
|In [3]: embed("@author/title")              |
|- - - - - - - - - - - - - - - - - - - - - - |
| +wrapper div-----------------------------+ | <--- note the lack of Out[3]:
| | +iframe------------------------------+ | |      because this is a side
| | | <link rel="style" href=.../>       | | |      effect of embed(), not
| | | <script> iframe_bundle.js </script>| | |      the return value of embed()
| | | <div> embed targets this div </div>| | |
| | | <script>                           | | |
| | |  This script, using functionality  | | |
| | |  from iframe_bundle.js, does these:| | |
| | |  - loads jsonified embed(inputs=[])| | |
| | |  - chooses cells embed(cells=[])   | | |
| | |  - monitors HTML body dimensions   | | |
| | |  - includes @observablehq/runtime  | | |     +observablehq.com+
| | |  - dynamically imports notebook    | | |     |                |
| | |     (await import('https://...'))  | | |     |                |
| | |    which may trigger many requests:| | |     |                |
| | |    request api.observablehq.com/@author/title.js?v=3----->    |
| | |       <-----JavaScript module for notebook------------        |
| | |    request api.observablehq.com/@mbostock/useful.js?v=3-->    |
| | |       <-----JavaScript module for another notebook----        |
| | |                                    | | |     +----------------+
| | |                                    | | |        +npm or CDN+
| | |    request cdn.jsdelivr.net/npm/d3@6---------------->      |
| | |       <-------------JavaScript module/script of dependency |
| | |    request cdn.jsdelivr.net/npm/moment-------------->      |
| | |       <-------------JavaScript module/script of dependency |
| | |</script>                           | | |        |          |
| | +------------------------------------+ | |        +----------+
| |    <a class="observable-link"          | |
| |     <span class="observable-logo">     | |
| |       Edit @author/title on Observable | |
| |     </span>                            | |
| |                                        | |
| | <script> wrapper_bundle.js </script>   | |
| |  - sets the .srcdoc of iframe above    | |
| |  - listens to iframe for size changes  | |
| +----------------------------------------+ |
+============================================+
```
