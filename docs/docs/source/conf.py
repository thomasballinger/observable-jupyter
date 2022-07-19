# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Observable Jupyter'
copyright = '2022, Ramiro Storni'
author = 'Ramiro Storni'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'nbsphinx',
	'sphinx_copybutton',
	'sphinx_gallery.load_style',
	'sphinx_design'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Thumb Nails -------------------------------------------------------------
nbsphinx_thumbnails = {
	'Bar_Chart_Race': 'Images/Thumbnails/Embed-Demo2.png',
	'Interactive_Map': 'Images/Thumbnails/Embedding_Demo.png',
	'World_Choroplath_Map': 'Images/Thumbnails/World_Map_Demo.png',
	'Linear_Regression': 'Images/Thumbnails/Linear_Regression.png',
	'Variable_Regression': 'Images/Thumbnails/Variable_Regression.png',
	'Faceting_Linear_Regression': 'Images/Thumbnails/Faceting_Linear_Regression.png',
	'Scatter_Plot_Scrub': 'Images/Thumbnails/Scrub_Filter_ScaterPlot.png',
	'Brushable_scatterplot': 'Images/Thumbnails/Brushable_ScatterPlot_Matrix.png',
	'Scatterplot_Matrix': 'Images/Thumbnails/ScatterPlot_Matrix.png',
	'Summary_Table': 'Images/Thumbnails/Summary_Table.png',
	'PixelValue_Intensity_Histogram': 'Images/Thumbnails/PixelValue_Intensity_Histogram.png'
	}

