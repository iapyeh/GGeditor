
.. _h36711971261f3518968783337294a20:

Tutorial
********

The GGeditor assumes a scenario that

#. you already have a project repository in the Github, and
#. you already have a project in the readthedocs.org which corresponds to that repository. 

Because that the Github and the readthedocs.org accept reStructuredText or markup formats only. You have to build the documentation in markup or reStructuredText formats. But you are suffering on creating document with markup or reStructuredText formats.

This is the flow chart of working with the GGeditor to build your documentations:

\ |IMG1|\ 

This tutorial would not go through all the possible routes in the flow chart. Here are the guidelines of what in this tutorial :

#. The tutorial will start from creating a new document in the Google Docs.
#. The new file will be named “Tutorial”. It has a heading, an image and an admonition which is created from the sidebar of the GGeditor.
#. The new file will be commit to the Github repository, in this demo, it is the repository of the GGeditor.
#. Because this is a new file, a process will be initiated for binding. It includes to login, navigate, create new file and commit.

It’s done for the “Tutorial” document. But we also want this “Tutorial” to be listed on the menu in the readthedocs project site. We have to add an item within the “toctree” in the index.rst. So there are extra steps when a new file was created:

#. Open the index.rst and add the new filename (“Tutorial”) in the table of toctree.
#. Commit the index.rst to the Github. 
#. Because the index.rst has already binded, we just need to click on the “Commit” button.

It’s done for the index.rst. If a document already has binding file, the process is simple --  open, edit and commit. This tutorial ends up by checking the project site in reatthedocs. You will see the “Tutorial” is online. We don’t need to do anything on the Github and the readthedocs. Because the readthedocs will automatically trigger a rebuild process when your repository has new committing.

Here is the video of this tutorial:

\ |IMG2|\ 


.. Note:: 

    #. When you name the Google Docs document, the name need not with suffix  “.rst”.
    #. But the binding file in the Github repository do need with suffix “.rst”. It will be automatically appended when the GGeditor created it. If you manually created the binding file, please name it with suffix “.rst”.

\ `The source document of this page in the Google Docs`_\ 



.. _`The source document of this page in the Google Docs`: https://docs.google.com/document/d/1V2Xync2yY9YYDHX6NJ5HXMekSnIIBi5035ephlAdJxA/edit?usp=sharing

.. |IMG1| image:: static/Tutorial_1.png
   :height: 464 px
   :width: 697 px

.. |IMG2| image:: static/Tutorial_2.png
   :height: 362 px
   :width: 641 px
   :target: https://goo.gl/XnWVSl
