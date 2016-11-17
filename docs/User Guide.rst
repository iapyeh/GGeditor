
.. _h177537546887b67276822514c66016:

How to Use
##########

.. _h2e2466207319265a2b484631c11587d:

The Google Docs Native Features
*******************************

Most features are just using the Google Docs’ native features. Such as

* Paragraph heading and indentation
* Bold , Italic, subscript and superscript
* List and numbered list
* Table
* Image and chart
* Footnote, hyperlink and bookmark
* Table of contents (links to bookmarks and headings)
* Horizontal line, special characters and CKJ full-width characters

.. _h80352f65a46575c6a74721e3ddb6a:

Inline Markups
**************

The table shows all the preserved inline markups of reST.


+---------------------------+----------------------------------+
|A \`single back-quote\`    |A `single back-quote`             |
+---------------------------+----------------------------------+
|A \`\`double back-quote\`\`|A ``double back-quote``           |
+---------------------------+----------------------------------+
|A \|replacement\| markup   |A \|replacement\| markup\ [#F1]_\ |
+---------------------------+----------------------------------+
|A \*\*emphasis\*\* text    |A **emphasis** text               |
+---------------------------+----------------------------------+

Besides the above list, you have more features by click the ``Show Markup Panel`` or the ``Commit to Github`` on the Add-ons/GGeditor menuitem.

\ |IMG1|\ 

.. _h19551a2a542b7a7919127f6f251b3817:

Show Markup Panel
*****************

This panel helps you to insert special markups and convert the document into reST file. There are three tabs in the panel.

.. _h1953454269561c41621765787c257114:

Markup Tab
==========

This tab is for adding admonitions, directives and cross-document “table of contents”.

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

\ `Directive`_\  is the generic form of admonition and many other reST Markups. ``Generic directive`` can be used for all kinds of directive. It will give you a table like below, you should replace all the placeholder to fit your needs.

\ |IMG3|\ 

This is an example of directive ``toctree``.

\ |IMG4|\ 

Please be noted that “name” and “content” is required, arguments and options are not. If there is no arguments, the placeholder should be removed. If there is no options, the options row (2nd row) can be deleted. If there is more than one options, they should be put line by line or row by row. 

\ |IMG5|\ 

This is what the above table generated reST:

\ |IMG6|\ 

You have to replace the name and content for your own purpose. One of the usage is to create customized admonition. The following directive table will create a ``And, by the way…`` dialog for you.

Below is how it is rendered in a web page.

.. admonition:: And, by the way...

    Here is your content

``Table of Contents`` will insert \ `a sphinx toctree`_\ , aka cross-document table of contents. Usually, this is inserted into the ``index.rst``.  All the documents with suffix .rst in the same folder will be inserted into the 3rd row. You have to adjust their order manually. Below is an example:

\ |IMG7|\ 

If a document was binding to another name, the binding name will be used. The document containing the table is not in the list for preventing from infinite loop while parsing. You should add it back manually if that makes sense for you.

The “maxdepth:2” means to build the sidebar based on “Parts” and “Chapter”.

You will see how it works in :ref:index

.. _h5a807c1a4a7d71c65729517f5c5635:

Style Tab
=========

This panel help user to adding headings to paragraphs. The headings construct the structure of the document. This panel shows the mapping of terminology between the Google Docs and the reStructuredText specification.

\ |IMG8|\ 

The lower section “Paragraph” is for styling normal text. ``Paragraph Content`` is for resetting style to normal text, ``Directive Content`` is for setting style to monospace. These two are usually used when you paste stuffs from other browser pages into the document.

\ |IMG9|\ 

.. _h6978575a60223f496c263254a447d32:

Conversion Tab
==============

\ |IMG10|\ 

.. _h76464c5c585d192b16121e3267e131:

Commit to Github
****************


.. _`Admonition`: http://read-the-docs.readthedocs.io/en/latest/_themes/sphinx_rtd_theme/demo_docs/source/demo.html?highlight=ADMONITION#admonitions
.. _`Directive`: http://docutils.sourceforge.net/docs/ref/rst/directives.html
.. _`a sphinx toctree`: http://www.sphinx-doc.org/en/1.4.8/markup/toctree.html


.. rubric:: Footnotes

.. [#f1]  If you manually put a substitution markup, you got to provide the replacement markup manually too.

.. |IMG1| image:: User_Guide/User_Guide_1.png
   :height: 105 px
   :width: 402 px

.. |IMG2| image:: User_Guide/User_Guide_2.png
   :height: 497 px
   :width: 309 px

.. |IMG3| image:: User_Guide/User_Guide_3.png
   :height: 156 px
   :width: 458 px

.. |IMG4| image:: User_Guide/User_Guide_4.png
   :height: 280 px
   :width: 426 px

.. |IMG5| image:: User_Guide/User_Guide_5.png
   :height: 396 px
   :width: 628 px

.. |IMG6| image:: User_Guide/User_Guide_6.png
   :height: 146 px
   :width: 150 px

.. |IMG7| image:: User_Guide/User_Guide_7.png
   :height: 153 px
   :width: 357 px

.. |IMG8| image:: User_Guide/User_Guide_8.png
   :height: 89 px
   :width: 240 px

.. |IMG9| image:: User_Guide/User_Guide_9.png
   :height: 326 px
   :width: 312 px

.. |IMG10| image:: User_Guide/User_Guide_10.png
   :height: 482 px
   :width: 312 px
