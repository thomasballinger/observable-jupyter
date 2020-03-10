# observable-jupyter-embed
<p align="center">

<a href="https://pypi.python.org/pypi/observable_jupyter">
<img src="https://img.shields.io/pypi/v/observable_jupyter.svg" /></a>
</p>

Embed cells from [Observable](https://observablehq.com/) notebooks into Jupyter notebooks.


These ways to view an example notebook won't work until we make this repository public:
* [Read example on nbviewer](https://nbviewer.jupyter.org/github/observablehq/observable_jupyter/blob/master/Observable_Embed_Example.ipynb)
* [Run example notebook on Binder]
* [Run example notebook on Colab]

To install the library, import the embed function, and embed the "graphic" cell from [this notebook](https://observablehq.com/@mbostock/epicyclic-gearing):
~~~py
!pip install observable_jupyter
from observable_jupyter import embed
embed('@mbostock/epicyclic-gearing', cells=['graphic'], inputs={'speed': 0.2})
~~~

The simplest way to use `embed()` is to render an entire Observable notebook:
~~~py
embed('@d3/gallery')
~~~

You may want to swap in your own data into a D3 chart:
~~~py
import this
text = ''.join(this.d.get(l, l) for l in this.s)
embed('@d3/word-cloud', cells=['chart'], inputs={'source': text})
~~~

With multiple cells, you can embed interactive charts!
~~~py
embed(
    '@observablehq/visualize-a-data-frame-with-observable-in-jupyter,
    cells=['vegaPetalsWidget', 'viewof sepalLengthLimits', 'viewof sepalWidthLimits'],
)
~~~
