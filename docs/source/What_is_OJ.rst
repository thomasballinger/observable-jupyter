=======================
Why Observable-Jupyter?
=======================

Observable Jupyter is a tool that allows for construction of quick
and reactive data visualizations. Leveraging the power of Observable
you have access to the countless visualizations created on the Observable platform.

.. note::

	If you are curious to learn about Observable and how it relates to Observable-Jupyter
	check out the :doc:`Understanding_the_Observable_in_OJ` section 


How it Works
------------

Observable-Jupyer makes use of Observable's APSs to essentaly connect a python environment like a Jupyter notebook 
or a Google Colabs notebook to an Observable notebook.

The process can be broken down into a couple of steps

First we call our embed function. Here we pass in the information we need from observable and the data we want to modiffy

From there the APIs retreve the data we need input our new data and run an observable notebook.

Once the notebook has run we then we embed it into our python environment.

What makes Observable-Jupyter so powerfull is that it is not limited to one data point.
