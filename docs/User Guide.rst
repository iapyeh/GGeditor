
#. How to Use

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

Some inline reST markups can be used directly in the document. The table shows all the usable inline markups.


+---------------------------+--------------------------------+
|In Google Docs document    |Rendered in html page           |
+===========================+================================+
|A \`single back-quote\`    |A `single back-quote`           |
+---------------------------+--------------------------------+
|A \`\`double back-quote\`\`|A ``double back-quote``         |
+---------------------------+--------------------------------+
|A \|replacement\| markup   |A |replacement| markup\ [#F1]_\ |
+---------------------------+--------------------------------+
|Text with \*\*emphasis\*\* |Text with **emphasis**          |
+---------------------------+--------------------------------+

.. |replacement| replace::   **replacement**

.. _h6c5e5e24234f72422a2ce37561f2355:

Markup Panel
************

\ |IMG1|\ 

Besides the above list, you have more features by click the ``Show Markup Panel`` or the ``Commit to Github`` on the Add-ons/GGeditor menuitem.

This “Show Markup Panel” helps you to insert special markups and convert the document into reST file. There are three tabs in the panel.

.. _h10487d767c3543552c4f797d453d593f:

Admonitions
===========

\ |IMG2|\ 

\ `Admonition`_\  is something like this:

.. Attention:: 

    Here is the content of this attention

There are 4 kinds of layout for 10 types of admonitions., please click on the admonition name, then it will be inserted as a table into your document. 

.. _h5a3b1c203613551578563c31657026b:

Directives
==========

\ |IMG3|\ 

\ `Directive`_\  is the generic form of admonition and many other reST Markups.

.. _h13a5d3e27e111c18554152c6d123c:

Generic Directive
-----------------

 ``Generic directive`` can be used for all kinds of reST directive. It will give you a table as shown below, you should replace all the placeholder to fit your needs.

\ |IMG4|\ 

The following table is an example of directive ``toctree``.

\ |IMG5|\ 

Please be noted that “name” and “content” are required, arguments and options are optional. If there is no arguments, the placeholder of arguments should be removed. If there is no options, the options row (2nd row) can be removed, or put your content in the 2nd row. If there is more than one options, these options should be put line by line or row by row. 

\ |IMG6|\ 

This is the reST generated from the above table.

\ |IMG7|\ 

You have to replace the name and content for your own purpose. One of the usage is to create customized admonition. The following directive table will create a ``And, by the way…`` dialog for you.

Below is how it is rendered in a web page.

.. admonition:: And, by the way...

    Here is your content

.. _h36d46272a794b2f694b492933796e5e:

Code
----

``code`` is for holding sample codes.

\ |IMG8|\ 

You can highlight your code by giving a language after \.\.code::, like this:

\ |IMG9|\ 

.. _ha1d6c3e373325355168491f521a78b:

Table of Contents
-----------------

``Table of Contents`` will insert \ `a sphinx toctree`_\ , aka cross-document table of contents to the cursor position. Usually, this is inserted into the ``index.rst`` document.  All the documents with suffix .rst in the same folder will be inserted into the 3rd row. Please be noted that file suffix (such as .html) is not required for the document name in list. Also, you have to adjust their order manually to fit your documentation plan. Below is an example:

\ |IMG10|\ 

If a document is binding a file in Github repository, the file name in Github will be used. The document which contains this toctree table is not in the list for preventing from infinite loop while parsing. You should add it back manually if that makes sense for you.

.. _h545b1150273f784141121a3967491529:

Headings
--------

\ |IMG11|\ 

The headings construct the structure of the document. If you put the cursor in a paragraph you can set the heading for that paragraph with this panel. You can click on the upper parts (such as Part, Chapter) or use the native heading tools of the Google Docs. The lower parts of this panel shows the relative headings in the Google Docs.

.. _h48253316368583f7c154246e606b2f:

Text Style
----------

\ |IMG12|\ 

If you put the cursor in a paragraph you can change the text style of that paragraph. The ``Paragraph Content`` is for resetting style to normal text, ``Directive Content`` is for setting style to monospace (code style). These two are usually used when you paste stuffs from other browser pages into the document.

.. _h742474725e04161204dc1d5b246619:

Misc
----

This is a panel for feature that is not been classified to a  category.

+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Name                |Description                                                                                                                                                                                                                                                                 |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Add link to document|Add a link of markup to other Google Docs document for selected text. Once clicked, a list of name of Google Docs will be prompted for your choice. Like this:                                                                                                              |
|                    |                                                                                                                                                                                                                                                                            |
|                    |\ |IMG13|\                                                                                                                                                                                                                                                                  |
|                    |                                                                                                                                                                                                                                                                            |
|                    |Please be noted that                                                                                                                                                                                                                                                        |
|                    |                                                                                                                                                                                                                                                                            |
|                    |#. only files in the same folder of the current document will be listed.                                                                                                                                                                                                    |
|                    |#. The Google Docs does not allow relative URL, so the added URL will be a pseudo-URL which starts with “http://cross.document/”, please keep the pseudo header when you are manually editing it. The pseudo-URL will be converted to relative-URL when generating the reST.|
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _h6978575a60223f496c263254a447d32:

Conversion Tab
==============

The Conversion tab has two buttons. 

\ |IMG14|\ 

The “Generate reST” will trigger the generating process and show the result in the area below that button.

\ |IMG15|\ 

The “Download” button let you download the generated reST and images in a zip file into your local PC.

.. _h76464c5c585d192b16121e3267e131:

Commit to Github
****************

.. _h767f774b5346d4195e437b31414f59:

Binding the document to a file in repository
============================================

You can provide your account and credentials for binding the document to a file in the Github repository. Here is the process diagram:

\ |IMG16|\ 

If you want to commit to a new file. Please

#. Navigate to the folder where the new file would be
#. Click on the “New File” item
#. Give the file name to create. The name will be suffix with “.rst” automatically.

.. _h572153e49969743e69262f2d637743:

Committing
==========

\ |IMG17|\ 

Once you have build the binding, next time you can use the “Commit” button directly to commit. You can reset the binding in this dialog too.

\ |IMG18|\ 

The “Rest Binding” is for rebinding the file in Github repository with this document.

\ |IMG19|\ 

If you just edited the text content only, you can uncheck “Commit images” to exclude images from committing. This would speed up the committing process.

.. _hb3e386c1329112c3f734c345c3396b:

About the Credentials
=====================

The credentials you given is encrypted and kept in the Google App Script platform. No any cloud server is built by the GGeditor.  You can uncheck “Remeber Github Credentials” checkbox or “Reset Credentials” button to clean up the stored credentials.

\ |IMG20|\ 

\ |IMG21|\ 


.. Caution:: 

    The GGeditor will never sent you emails to request reset credentials or anything else.

You can give the credentials every time doing the committing. Like the following image shows.

\ |IMG22|\ 


.. _`Admonition`: http://read-the-docs.readthedocs.io/en/latest/_themes/sphinx_rtd_theme/demo_docs/source/demo.html?highlight=ADMONITION#admonitions
.. _`Directive`: http://docutils.sourceforge.net/docs/ref/rst/directives.html
.. _`a sphinx toctree`: http://www.sphinx-doc.org/en/1.4.8/markup/toctree.html


.. rubric:: Footnotes

.. [#f1]  If you manually put a substitution markup, you got to provide the replacement markup manu

.. |IMG1| image:: user_guide/user_guide_1.png
   :height: 105 px
   :width: 402 px

.. |IMG2| image:: user_guide/user_guide_2.png
   :height: 216 px
   :width: 280 px

.. |IMG3| image:: user_guide/user_guide_3.png
   :height: 166 px
   :width: 276 px

.. |IMG4| image:: user_guide/user_guide_4.png
   :height: 156 px
   :width: 458 px

.. |IMG5| image:: user_guide/user_guide_5.png
   :height: 280 px
   :width: 426 px

.. |IMG6| image:: user_guide/user_guide_6.png
   :height: 364 px
   :width: 773 px

.. |IMG7| image:: user_guide/user_guide_7.png
   :height: 130 px
   :width: 140 px

.. |IMG8| image:: user_guide/user_guide_8.png
   :height: 68 px
   :width: 560 px

.. |IMG9| image:: user_guide/user_guide_9.png
   :height: 108 px
   :width: 558 px

.. |IMG10| image:: user_guide/user_guide_10.png
   :height: 153 px
   :width: 357 px

.. |IMG11| image:: user_guide/user_guide_11.png
   :height: 133 px
   :width: 266 px

.. |IMG12| image:: user_guide/user_guide_12.png
   :height: 84 px
   :width: 265 px

.. |IMG13| image:: user_guide/user_guide_13.png
   :height: 236 px
   :width: 246 px

.. |IMG14| image:: user_guide/user_guide_14.png
   :height: 36 px
   :width: 108 px

.. |IMG15| image:: user_guide/user_guide_15.png
   :height: 38 px
   :width: 81 px

.. |IMG16| image:: user_guide/user_guide_16.png
   :height: 545 px
   :width: 664 px

.. |IMG17| image:: user_guide/user_guide_17.png
   :height: 304 px
   :width: 600 px

.. |IMG18| image:: user_guide/user_guide_18.png
   :height: 40 px
   :width: 105 px

.. |IMG19| image:: user_guide/user_guide_19.png
   :height: 52 px
   :width: 152 px

.. |IMG20| image:: user_guide/user_guide_20.png
   :height: 29 px
   :width: 213 px

.. |IMG21| image:: user_guide/user_guide_21.png
   :height: 38 px
   :width: 128 px

.. |IMG22| image:: user_guide/user_guide_22.png
   :height: 404 px
   :width: 688 px
