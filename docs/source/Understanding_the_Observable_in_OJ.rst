=========================================
Relating Observable to Observable-Jupyter
=========================================

Observable-Jupyter would not exist without Observable and yet
you might be asking yourself the excelent questions: *What is Observable?* 
and *How do these two programs related?* 

What is Observable?
-------------------
At a fundamental level Observable is a software similar to Jupyter notebooks and Google Colabs. It allows users to write code and markdown in a series
of cells. However, it differs in that Observable Notebooks are reactive and written in Javascript. 

These two freatures of Observable are what make it a great tool for data visualization. 

.. card:: 

    Javascript
    ^^^
    Javascript gives Observable users access to great visualization and charting
    libraries like d3 and observable plot among others.
    

.. card::           

    Reactivity
    ^^^
    Reactivity makes it so that a change in one cell will then trigger changes other associated cells meaning
    any modification in the data processing pipeline will automaticaly be expressed in a visualization.

Observable Community
--------------------

Observable is not just software. It is also a community of data practitioners who are passionate
about visualization.

All published Notebooks on Observable are open source and it is common for users to build off of eachothers work. 
This is great news for us Observable-Jupyter users since it means that there are countless visualizations at our 
finger tips that we can simply modify, embed, and use in our own projects.


Observable Vs Observable-Jupyter
--------------------------------
 
It is best to think of Observable-Jupyter as a program that works in collaboration with Observable.

Given that a majority of the data science community works with python, Observable Jupyter looks to introduce python 
users to Observable by giving them access to visualizations that are made with powerful visualization libraries like d3. 

Observable-Jupyter gives python users access to Observable visualizations by using APIs provided by Observable to pass data back and forth essentialy allowing python users to modify
existing Observable notebooks for their own personal projects. 

.. note::
   Check out how to embed visualizations into your own project in the :doc:`Embedding_cells` section. 


Additional Observable Resources
-------------------------------

| Interested in learning more about Observable?
| Take a look at the following links:

.. hlist::
   :columns: 1
   
   * :bdg-link-primary-line:`Obsevable<https://observablehq.com/explore>`
   * :bdg-link-primary-line:`Observable for Jupyter Users<https://observablehq.com/@observablehq/observable-for-jupyter-users>`
   * :bdg-link-primary-line:`Visualize a data frame with Observable, in Jupyter<https://observablehq.com/@observablehq/visualize-a-data-frame-with-observable-in-jupyter>`
