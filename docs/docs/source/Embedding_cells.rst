===============
Embedding Cells
===============
The embed function is the backbone of Observable-Jupyter and the only function you will need
to get stunning visualizations to populate on your screen.

To begin embedding Observable Visualizations into your project you will first import the function from
Observable-Jupyter.

.. code:: Python

   from observable_jupyter import embed

.. note::
   | Having trouble importing the embed function?
   | Make sure you have properly installed the program by following the instructions on the :doc:`Installation` section. 

Embed Function
--------------

.. py:function:: embed(partial_URL, cell = [ "" ], inputs = { "" : None} )

   :param partial_URL: Parital URL from an Observable Notebook.
   :param cell: Optional -- cells to be displayed.
   :param inputs: Optional -- variables to be manipulated.
   :type partial_URL: str
   :type cell: list[str] or None
   :type inputs: dict(str : None) or None
   :return: Observable Visualization 
   :rtype: svg

.. note::
   If no parameters are passed for cell the entire Observable Notebook will become embedded into your project. Additionaly,
   if no parameters are passed for inputs the values assigned in the Observable Notebook will be used.

Rendering Visualizations
-------------------------
To render visualizations in a project call the embed function and pass in the desired arguments.

For this example we want to use a visualization found in the following Observable notebook:
https://observablehq.com/@mbostock/epicyclic-gearing.

.. important::
   
   Unsure as to where the URL being used came from? Make sure to read the
   :doc:`Understanding_the_Observable_in_OJ` section to learn about Observable and how it
   relates to Observable-Jupyter.

.. code:: Python

   from observable_jupyter import embed
   embed('@mbostock/epicyclic-gearing',
	  cells=['graphic'],
	  inputs={'speed': 0.2}
	)

So what did that code just do?

1. First we imported the embed function
2. Next we called the function and passed in three arguments
3. The first is the path for the desired notebook we want to embed from
4. Then the second argument defines what cells from the notebook notebook we want to render
5. Finaly the third argument allows us to define values for public variables found in the notebook

To play around with the code yourself check out this link to a Google Colabs notebook with the code
found on this page: :bdg-link-primary-line:`Embedding Cells Demo <https://colab.research.google.com/drive/123a6Sg13pvdyHxzqOgXIwX38qtP264zQ?usp=sharing>`

.. note::
   
   Notice how the first argument is everything that comes after **https://observablehq.com/**
   in the URL **https://observablehq.com/@mbostock/epicyclic-gearing**. 
   

Modifying Variables
-------------------

Once you know how to use the embed function it could be fun to start playing arround with variables to change aspects of
your visualization.

To get the most out the ability to change variables you need to know a little bit about the observable notebook you are chosing to embed in your code.
In particular you should try to get familiar with what exposed variables effect the visualization.


.. tip::
   If going into Observable and deciphering what each variable does seems a little too daunting, take a look at the :doc:`Visualization_Library`. There we have done the heavy lifting 
   of exposing all necessary variables and explaining what they do. 

   While this is useful for common visualizations it can be limiting if you want to fully costomize a visualization.

Take the example from the embedding demo. If we look into the Observable notebook we learn that there are many variables that will change the visualization:

.. hlist::
   :columns: 2

   * speed
   * toothRadius
   * holeRadius
   * frameAngle
 
By including exposed variables in our inputs parameter we have the ability to modify their values and ultimately alter the behaviour of our visualization.

.. code:: Python

   from observable_jupyter import embed
   embed('@mbostock/epicyclic-gearing',
          cells=['graphic'],
          inputs={'speed': 0.2,
		  'toothRadius' : 0.01,
		  'holeRadius' : 0.03,
		  'frameAngle' : 22
		 }
        )

Try this out for yourself by playing around with the modified code on the Google Colabs Notebook linked here: :bdg-link-primary-line:`Modifying Variables Demo 
<https://colab.research.google.com/drive/1JGVE6bKQ18omUMzTIvxaJKOIjmLGVVAD?usp=sharing>`

Next Steps
----------

| While simple, this concept of modifying variables holds a lot of power.

For example given any visualization you have the ability to inject your own data by modifying a few variables. 
Depending on the visualization and how it was originaly written in Observable getting a functioning visualization after modifing variables
can become a bit chalenging.

| Luckily if you are interested some of those challenges are adressed in the :doc:`Using_your_own_data` section.

