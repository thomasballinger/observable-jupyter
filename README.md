# observable-jupyter-embed
<p align="center">

<a href="https://pypi.python.org/pypi/observable_jupyter_embed">
<img src="https://img.shields.io/pypi/v/observable_jupyter_embed.svg" /></a>
<a href="https://travis-ci.org/thomasballinger/observable_jupyter_embed"><img src="https://travis-ci.org/thomasballinger/observable_jupyter_embed.svg?branch=master" /></a>
</p>
Embed Observable cells hosted on observablehq.com into Jupyter notebooks.

Name is not final.

This module is not released yet.

~~~py
from observable_jupyter_embed import embed
embed('d/e4d7b23b27074e16', inputs={'a': [1,2,3], 'b': 4}, use_iframe=False)
~~~

# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
