# observable-jupyter-embed
<p align="center">

<a href="https://pypi.python.org/pypi/observable_jupyter">
<img src="https://img.shields.io/pypi/v/observable_jupyter.svg" /></a>
<a href="https://travis-ci.org/observablehq/observable_jupyter"><img src="https://travis-ci.org/thomasballinger/observable_jupyter.svg?branch=master" /></a>
</p>
Embed Observable cells hosted on observablehq.com into Jupyter notebooks.

~~~py
!pip install observable_jupyter
from observable_jupyter import embed
embed('d/e4d7b23b27074e16', inputs={'a': [1,2,3], 'b': 4})
~~~

Render the entire notebook Observable notebook:
~~~py
embed('d/e4d7b23b27074e16')
~~~

See [this Observable notebook](https://observablehq.com/d/e91855e8f5b3b7) for more info.

# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
