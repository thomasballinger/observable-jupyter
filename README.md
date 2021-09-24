# observable_jupyter

<p align="center">
<a href="https://pypi.python.org/pypi/observable_jupyter">
    <img src="https://img.shields.io/pypi/v/observable_jupyter.svg" />
</a>
<a href="https://github.com/thomasballinger/observable-jupyter">
    <img src="https://img.shields.io/github/checks-status/thomasballinger/observable-jupyter/main"/>
</a>
</p>

Embed cells from [Observable](https://observablehq.com/) notebooks into Jupyter notebooks.

[View demo notebook on Colab](https://colab.research.google.com/drive/1t_wcE-NqoPO-dpnrB9VMQ0KUxR5e1rML?usp=sharing)

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

## About this library

This is an unofficial, but unlikely to break because it uses official embedding APIs, library for embedding Observable notebooks in Jupyter.
The library was developed at Observable but is now maintained by Thomas Ballinger.
All code added before Sept 2021 is copyright Observable.


## Development

Because this is a Python and JavaScript library, you'll need node as well as Python to contribute to it.
