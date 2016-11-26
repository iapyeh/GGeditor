
.. _h36711971261f3518968783337294a20:

Tutorial
********

The GGeditor assumes a scenario that

#. you already have a project repository in the Github, and
#. you already have a project in the readthedocs.org which corresponds to that repository. 

Because the Github and the readthedocs.org accept reStructuredText or markup formats only. You have to build documentation in markup or reStructuredText formats. But you are suffering on creating document with markup or reStructuredText formats.

This is the flow chart of working with the GGeditor to build your documentation:

\ |IMG1|\ 

This tutorial would only go through the longest route in the flow chart. Here are the sequences of what are been demonstrated in this tutorial :

#. The tutorial will start from creating a new document in the Google Docs.
#. The new file will be named “Tutorial”. It has a heading, an image and an admonition which is created from the sidebar of the GGeditor.
#. The new file will be commit to the Github repository, in this demo, it is the repository of the GGeditor.
#. Because this is a new file, a process will be initiated for binding. It includes to login, navigate, create new file and commit.

It’s done for the “Tutorial” document.


.. Warning:: 

    For CKJ users: (繁體中文、简体中文、한국어、日本語)
    
    English document name is strongly suggested for naming your documents. Especially when the document contains images. Because images got pathname from their hosting document. Naming document in English would reduce risk of parsing failure in the readthedocs.org.

Because we also want the document “Tutorial”  to be listed on the menu in the readthedocs project site. We have to add an item within the “toctree” in the index.rst. So there are extra steps when a new file was created:

#. Open the index.rst and add the new filename (“Tutorial”) in the table of toctree.
#. Commit the index.rst to the Github.  Because the index.rst has already binded, we just need to click the “Commit” button.

It’s done for updating the index.rst. 

If a document already has a binding file, the process is simple, just to  open, edit and commit. This tutorial ends up by checking the project site in reatthedocs.org. You will see the content of this new document “Tutorial” is on the project site of the readthedocs.org. We don’t need to do anything on the Github or the readthedocs.org. Because the readthedocs.org will automatically rebuild your project site when the corresponding repository move forward.

Here is the video of this tutorial:

\ |IMG2|\ 


.. Note:: 

    #. When you name the Google Docs document, the name need not with suffix  “.rst”.
    #. But the binding file in the Github repository do need with suffix “.rst”. It will be automatically appended when the GGeditor created it. If you manually created the binding file, please name it with suffix “.rst”.
    #. in this tutorial video, the committing of index.rst does not also commit images. That is because the changes include text part only.  By unchecking the “Commit images” option, the committing only updates the generated reStructuredText content of the index.rst. Which makes the time of committing being shorter.

\ |LINK1|\ 



.. |LINK1| raw:: html

    <a href="https://docs.google.com/document/d/1V2Xync2yY9YYDHX6NJ5HXMekSnIIBi5035ephlAdJxA/edit?usp=sharing" target="_blank">The source document of this page in the Google Docs</a>


.. |IMG1| image:: static/Tutorial_1.png
   :height: 464 px
   :width: 697 px

.. |IMG2| image:: static/Tutorial_2.png
   :height: 362 px
   :width: 641 px
   :target: https://goo.gl/XnWVSl
