# Documentation

Contributing to documention on readthedocs.org

## Setup and build the HTML

Install Sphinx and build the HTML documentation

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
make html
open build/html/index.html
```

## Add a demo to the Gallery

* Create a jupyter notebook that runs an observable-jupyter visualization
* Create a thumbnail (right now we do this with a screen shot) and put it in source/thumbnail/images
  * Sphinx looks for this thumbnail in the Jupyter notebook, the notebook should have the following line...
  ```
  ADD THE CODE HERE
  ```
* Put the notebook in ./source
* Add an entry for the thumbnail in source/conf.py to the `nbsphinx_thumbnails` dictionary
* Add an entry for the notebook in source/VisualizationLibrary.rst
* Rebuild the HTML (see above)

## Seeing your changes

* Push Branch to Github 
* Once pull a pull request is accepted readthedocs will be updated

