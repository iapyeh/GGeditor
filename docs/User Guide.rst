
.. _h177537546887b67276822514c66016:

How to Use
##########

Most features are just using the Google Docs’ native widgets. Such as

* Paragraph heading and indentation
* Bold , Italic, subscript and superscript
* List and numbered list
* Table
* Image and chart
* Footnote, hyperlink and bookmark
* Table of contents (links to bookmarks and headings)
* Horizontal line, special characters and CKJ full\-width characters

Besides the above list, you have more features by click the ``Show Markup Panel`` or the ``Commit to Github`` on the Add\-ons/GGeditor menuitem.

\ |IMG1|\ 

.. _h19551a2a542b7a7919127f6f251b3817:

Show Markup Panel
*****************

This panel helps you to insert special markups and convert the document into reST file. There are three tabs in the panel.

.. _h1953454269561c41621765787c257114:

Markup Tab
==========

This tab is for adding admonitions, directives and cross\-document “table of contents”.

\ |IMG2|\ 

.. _h10487d767c3543552c4f797d453d593f:

Admonitions
===========

\ `Admonition`_\  is something like this:

.. Attention:: 

    Here is the content of this attention

Click on the admonition name, then it will be inserted as a table into your document.

.. _h5a3b1c203613551578563c31657026b:

Directives
==========

Directive is the generic form of admonition and many other reST Markups. `Generic directive` can be used for all kinds of directive. It will give you a table like this:

+-----------------+
|\.\. name\:\:    |
+-----------------+
|(content of name)|
+-----------------+

You have to replace the name and content for your own purpose. One of the usage is to create customized admonition. The following directive table will create a ``And, by the way…`` dialog for you.

+--------------------------------------+
|\.\. admonition\:\: And, by the way...|
+--------------------------------------+
|Here is your content                  |
+--------------------------------------+


.. admonition:: And, by the way...

    Here is your content

.. _h2c1d74277104e41780968148427e:




.. _h5a807c1a4a7d71c65729517f5c5635:

Style Tab
=========

\ |IMG3|\ 

.. _h6978575a60223f496c263254a447d32:

Conversion Tab
==============

\ |IMG4|\ 

.. _h76464c5c585d192b16121e3267e131:

Commit to Github
****************


.. _`Admonition`: http://read-the-docs.readthedocs.io/en/latest/_themes/sphinx_rtd_theme/demo_docs/source/demo.html?highlight=ADMONITION#admonitions

.. |IMG1| image:: User_Guide/User_Guide_1.png
   :height: 105 px
   :width: 402 px

.. |IMG2| image:: User_Guide/User_Guide_2.png
   :height: 497 px
   :width: 309 px

.. |IMG3| image:: User_Guide/User_Guide_3.png
   :height: 326 px
   :width: 312 px

.. |IMG4| image:: User_Guide/User_Guide_4.png
   :height: 482 px
   :width: 312 px
