
.. _h177537546887b67276822514c66016:

How to Use
**********

.. _h2e2466207319265a2b484631c11587d:

The Google Docs Native Features
===============================

You can use the following list native features of the Google Docs to build your content for generating reStructuredText format.

* Paragraph heading and indentation

* Bold, Italic, subscript and superscript

* List and numbered list

* Table

* Image and chart

* Footnote, hyperlink and bookmark

* Table of contents (links to bookmarks and headings)

* Special characters and CKJ full-width characters

* Horizontal line

..  Note:: 

    A hyperlink will be opened in a new window(tab) if its URL is of format “scheme://…”, like http://, https://, etc.

.. _h80352f65a46575c6a74721e3ddb6a:

Inline Markups
==============

Some inline reStructuredText markups can be used directly in the document. The table below shows the usage example of these inline markups.


+---------------------------+-----------------------+
|In Google Docs document    |Rendered in HTML page  |
+===========================+=======================+
|A \`single back-quote\`    |A `single back-quote`  |
+---------------------------+-----------------------+
|A \`\`double back-quote\`\`|A ``double back-quote``|
+---------------------------+-----------------------+
|A \|replacement\| markup   |A |replacement| markup |
+---------------------------+-----------------------+

.. |replacement| replace::   **replaced**

That is converted from the source content in document:

\ |IMG1|\ 

Please noted that if you manually put a substitution markup, you got to provide correct replacement markup manually too. Otherwise, the sphinx parser will raise exception. 

.. _h513c5b795d5d185d1c203d7e75205f41:

Table
=====

The Google Docs native table can be converted to reStructuredText table. One thing must mention is that, if you want to generate header rows in the generated reStructuredText table, you have to make all text in the header rows to be bold.

\ |IMG2|\ 

This is the rendered table of the above content.


+----------+----------+----------+
|Header Row|Header Row|Header Row|
+==========+==========+==========+
|Normal Row|Normal Row|Normal Row|
+----------+----------+----------+
|Normal Row|Normal Row|Normal Row|
+----------+----------+----------+


..  Hint:: 

    You can set background-color for header rows by assign CSS in the /docs/static/theme_overrides.css. For example:
    
    .wy-table-responsive table th {
       background-color: #f0f0f0;
    }

.. _h425360541a6d36a14487962c584b8:

Image
=====

Images and charts in the Google Docs document are able to be converted to the generated reStructuredText file bundles. Here is the naming rules:

#. A folder named “static” will be created if necessary in the same folder of the document.

#. All the images in the document will be stored in the “static” folder in PNG format. 

#. The image name is the document name + underscore + sequence number + ‘.png’

Images will be re-generated if “Commit images” was checked. That is, the mapping between image content and image name might not be constant.

..  Warning:: 

    For CKJ users: (繁體中文、简体中文、한국어、日本語)
    
    English document name is strongly suggested for naming your documents. Especially those documents with images because an image got pathname from its hosting document. By naming document in English, it would reduce the risk of parsing failure in the readthedocs.org.


..  Note:: 

    Currently, it seems the sphinx parser has problem on parsing :align: of an image markup, so image horizontal alignment is not supported yet. 

.. _h15691d2ce397119197a3a1434795f3e:

Add-ons Menu Item of GGeditor
=============================

\ |IMG3|\ 

You can access the following features from the add-on menu item of GGeditor.

.. _h6c5e5e24234f72422a2ce37561f2355:

Markup Panel
============

The “Show Markup Panel” helps you to insert special markups, to see the converted content in reStructuredText, or to download the generated files.

.. _h10487d767c3543552c4f797d453d593f:

Admonitions
-----------

\ |IMG4|\ 

\ |LINK1|\  is something like this:

..  Attention:: 

    Here is the content of this attention

The GGeditor try to set the look-and-feel of admonitions to be as close as possible to what they are in the readthedocs.org (RTD). There are 4 kinds of layout for 10 types of admonitions. Please click on the admonition name to insert them into your document.

.. _h584616187e1a7c33197e463470237f12:

Custom Admonition
-----------------

The “custom” at lower-right of the admonitions panel is a special feature. It inserts a template of admonition. In the diagram below, the left side is the template and you should change its title to whatever you want. The GGeditor will convert it to native markup of reStructuredText.

\ |IMG5|\ 

It renders like this:

.. admonition:: Release Note

    (content of Change-me)

.. _h5a3b1c203613551578563c31657026b:

Directives
----------

\ |LINK2|\  is the generic form of admonition and many other reST Markups.

.. _h13a5d3e27e111c18554152c6d123c:

Generic Directive
~~~~~~~~~~~~~~~~~

\ |IMG6|\ 

 ``Generic directive`` can be used for all kinds of reST directive. It will give you a table as shown below, you should replace all the placeholder to fit your needs.

\ |IMG7|\ 

The following table is an example of the directive ``toctree``.

\ |IMG8|\ 

Please be noted “name” and “content” are required for a directive, arguments and options are optional. If there are no options, the content can be in the 2nd row. If there is more than one options, these options should be put line by line in 2nd row, or row by row. See the diagram below for illustration. 

\ |IMG9|\ 

This is the reST generated from the above table.

\ |IMG10|\ 

You have to replace the name and content for your own purpose. One of the usage is to create customized admonition. The following directive table will create a ``And, by the way…`` dialog for you.

\ |IMG11|\ 

Below is how it is rendered in the web page.


.. admonition:: And, by the way...

    Here is your content

.. _h36d46272a794b2f694b492933796e5e:

Code
~~~~

\ |IMG12|\ 

``code`` is for holding sample codes.

\ |IMG13|\ 

The content in a code directive cannot be in bold or italic. Neither hyperlinks and images.

You can highlight your code by giving a language name after the \.\.code::, like this: (there is a space in front of “python”)

\ |IMG14|\ 

It is rendered like this:


.. code:: python

    #!/usr/bin/env python
    
    """
    Twisted moved the C{twisted} hierarchy to the C{src} hierarchy, but C{git}
    doesn't know how to track moves of directories, only files.  Therefore any
    files added in branches after this move will be added into ./twisted/ and need
    to be moved over into 
    """
    
    import os
    from twisted.python.filepath import FilePath
    
    here = FilePath(__file__).parent().parent()
    fromPath = here.child("twisted")
    toPath = here.child("src")
    
    for fn in fromPath.walk():
        if fn.isfile():
            os.system("git mv {it} src/{it}"
                      .format(it="/".join(fn.segmentsFrom(here))))
    
    os.system('git clean -fd')

.. _h19332e5f3041595843151e66556b374:

Code with line number
~~~~~~~~~~~~~~~~~~~~~

\ |IMG15|\ 

This will insert a "code-block" directive. This feature render the given content with line numbers. The ":linenos" option should not be removed. Because the "code-block" should have an argument for programming language of the given content, a placeholder "python" has been appended as default. This argument can be replaced but shall not been removed.

\ |IMG16|\ 


.. code-block:: python
    :linenos:

    #!/usr/bin/env python
    
    """
    Twisted moved the C{twisted} hierarchy to the C{src} hierarchy, but C{git}
    doesn't know how to track moves of directories, only files.  Therefore any
    files added in branches after this move will be added into ./twisted/ and need
    to be moved over into 
    """
    
    import os
    from twisted.python.filepath import FilePath
    
    here = FilePath(__file__).parent().parent()
    fromPath = here.child("twisted")
    toPath = here.child("src")
    
    for fn in fromPath.walk():
        if fn.isfile():
            os.system("git mv {it} src/{it}"
                      .format(it="/".join(fn.segmentsFrom(here))))
    
    os.system('git clean -fd')

.. _ha1d6c3e373325355168491f521a78b:

Table of Contents
~~~~~~~~~~~~~~~~~

\ |IMG17|\ 

The Table of Contents will insert \ |LINK3|\ , aka cross-document table of contents to the cursor position. Usually, it was inserted into the ``index.rst`` document.  The rules of what filename been included in the auto generated toctree table are:

#. All the documents with suffix .rst in the same folder of this document. Even the document is not binding to a file in the Github.

#. If a document is binding to a file in the Github, the filename will be used. Even the source document is not with suffix “.rst”.

#. The current document is excluded. This is for preventing from falling into an infinite loop while the RTD parsing this table. You should add it back manually if that makes sense for you.

 Here is an example of what it looks like:

\ |IMG18|\ 

Please be noted the file suffix (.html or .rst) has been omitted. Also, you have to change their order manually.  You have to manually edit the list content in the 3rd row when you add or remove your documents. Maybe you can just ask the GGeditor to generate a new doctree table and remove the existing one. You can refer to \ |LINK4|\  of the GGeditor for an example.

Raw HTML

\ |IMG19|\ 

This is a handy feature for you to embed html tags into the generated reStructuredText file. This button will insert a table into the document. Then you can put HTML tages in the table.  The GGeditor will convert the table content to a ".. raw:: html" directive.

.. _h545b1150273f784141121a3967491529:

Headings
~~~~~~~~

\ |IMG20|\ 

The headings construct the structure of the document. If you put the cursor in a paragraph you can set the heading for that paragraph with this panel. You can click on the upper parts (like Part, Chapter) or use the native heading tools of the Google Docs. The lower parts of this panel shows the relative headings in the Google Docs.

.. _h48253316368583f7c154246e606b2f:

Text Style
~~~~~~~~~~

\ |IMG21|\ 

By putting the cursor in a paragraph you can change the text style of that paragraph. The `Paragraph Content` is for normal text, `Directive Content` is for code style (monospace). These two are usually used when you paste stuffs from other browser pages into your document.

.. _h6a6d21367d4a577c6e29134f4b4566:

Upgrade all headings
~~~~~~~~~~~~~~~~~~~~

All the paragraphs with headings will increase one level of heading. That is, Heading 2 becomes Heading 1, and Heading 1 becomes Title. Heading 6 becomes Heading 5. Title keeps Title. 

This is useful when you dealing with depth level about what will be listed on the sidebar of your project site in the RTD.

.. _h718131c7b26674c67184b5c254e2418:

Downgrade all headings
~~~~~~~~~~~~~~~~~~~~~~

All the paragraphs with headings will decrease one level of heading. That is, Heading 1 becomes Heading 2, and Title becomes Heading 1.  Heading 5 becomes Heading 6. Heading 6 keeps Heading 6.

.. _h2b1187163654202538b4a3d40663:

Add link to another document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a link of markup to other Google Docs document for selected text. Once clicked, a list of name of Google Docs will be prompted for your choice. Like this:

\ |IMG22|\ 

Please be noted:

#. only files in the same folder of the current document will be listed.

#. The Google Docs does not allow relative URL, so the added URL will be a pseudo-URL which starts with “http://cross.document/”, please keep the pseudo header when you are manually editing it. The pseudo-URL will be converted to relative-URL when generating the reST.

.. _h76464c5c585d192b16121e3267e131:

Commit to Github
================

.. _h767f774b5346d4195e437b31414f59:

Binding the document to a file in repository
--------------------------------------------

You can provide your account credentials for binding the document to a file in the Github repository. Here is the process diagram:

\ |IMG23|\ 

If you want to commit to a new file. Please

#. Navigate to the folder where the new file would be

#. Click on the “New File” item

#. Give the file name to create. The name will be suffix with “.rst” automatically.


..  Hint:: 

    While doing any clicking, ONE click is enough. No need to do “Double-Clicking”.

.. _h2c1d74277104e41780968148427e:




.. _h572153e49969743e69262f2d637743:

Committing
----------

\ |IMG24|\ 

Once you have build the binding, next time you can use the “Commit” button directly to commit. You can reset the binding in this dialog too.

\ |IMG25|\ 

The “Rest Binding” is for rebinding the file in Github repository with this document.

\ |IMG26|\ 

If only the text content has been modified, you can un-check the “Commit images” to exclude images from committing. This would speed up the committing process.

..  Note:: 

    The GGeditor will maintain image files it uploaded to the Github repository while committing. If you modified any image, no matter adding, replacement or deletion, you should check “Commit images”.


..  Attention:: 

    If you have a fat document like this one "How to User", which has lots of images to upload, you might experience broken images in its corresponding html page in your RTD web site. It is because the RTD re-generating the html when uploading is still ongoing. In that case, you have to wait longer for the RTD to release its lock of building or enforce the RTD to build again from your administration page.
    
    By the way, if you see an obsoleted image the reason might be that the RTD set cache time longer. In that case, you can clear the browser cache or check the Github repository for figuring what happened.

.. _hb3e386c1329112c3f734c345c3396b:

About the Credentials
---------------------

Given credentials is encrypted and kept in the Google App Script platform. None cloud server is built by the GGeditor. 

\ |IMG27|\ \ |IMG28|\ 

Credentials is optional. You can un-check the “Remember Github Credentials” check box or the “Reset Credentials” button to clean up the stored credentials.


..  Caution:: 

    The GGeditor will never sent you email to request reset credentials or anything else.

.. _h3b4f503332637854223493a2d2f21b:

Conversion
==========

\ |IMG29|\ 

When you open the conversion dialog, the conversion process will be starting. When the conversion has completed, you can copy the generated reStructuredText content to clipboard by "Copy to Clipboard" button, or download the generated reStructuredText content as well as images by the "Download" button.

.. _h7271646e36a33751612c195c3e53e:

Conversion Rules
----------------

What been converted depends on selection and the cursor position, rules are:

#. If there are selections, the top elements of every selected one are converted. Which means if a paragraph is partially selected, whole the paragraph is converted.

#. If there is no selection and the cursor is in a table, that table is converted

#. Otherwise, the whole document is converted

The conversion message on the right side are indications. There are three kinds of message:

\ |IMG30|\ Means the whole document is converted to the reStructuredText format.

\ |IMG31|\ Means only the table where cursor positioned was converted to the reStructuredText format. (partial conversion)

\ |IMG32|\ Means only the selection was converted to the reStructuredText format.  (partial conversion)

.. _h5782051373e754c6735481f7d792d67:

Why Partial Conversion
----------------------

The idea for partial conversion is mainly for creating comments in a source code. In your source code scripts, you can have comments for functions, classes, modules, packages in reStructuredText format. The RTD can automatically generate API documents from source codes. This "\ |LINK5|\ " has more.

.. _h95148cc6506117925452e78c21:

Copy to Clipboard
-----------------

\ |IMG33|\ 

(This feature is specially for API writers, so it is only visible for partial conversion)

This button will copy the generated reStructuredText to system clipboard (pasteboard). For convenience to paste as a block of comment in source code, you can assign a prefix for every copied line. The options are:


+---------+------------------------------+
|Options  |Note                          |
+=========+==============================+
|No prefix|                              |
+---------+------------------------------+
|#        |Python                        |
+---------+------------------------------+
|\*       |Javascript, C++, Java, … etc  |
+---------+------------------------------+
|//       |Javascript, C++, Java, ... etc|
+---------+------------------------------+
|Ask      |whatever you say              |
+---------+------------------------------+

.. _h6f1f457d4147275ff141e245c44e79:

Dowload
-------

\ |IMG34|\ 

What been converted depends on selection and the cursor position, rules are:

#. When partially converted, a  <document-name>_selection.zip or  <document-name>_table.zip will be created with the partially generated reStructuredText content and images (if any).

#. If whole document is converted, a <document-name>.zip will be created with whole generated reStructuredText content and images (if any).

.. _hb512c40675e711967718345c60723c:

Generate Document
-----------------

\ |IMG35|\ 

When partial content is converted only, like table or selection, The "Generate Document" button appears. Users can click this button to enforce the whole document is converted.

.. _hc97272434561d31f5d3b294a205c:

Settings
========

.. _h656c5e2450654757441516265f2921:

Accounts
--------

The GGeditor supports multipe Github accounts. You can select the account to use when committing converted reStructuredText to the Github for every single document. This panel is where you manage these Githubs accounts.

\ |IMG36|\ 

.. _h3a106f1e4d7d526393a6657d142f5d:

Document Preferences
--------------------

\ |IMG37|\ 

.. _h204e7726715c28365f3825e59381a28:

When converting tables in this document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have two options.

"with pure reStructuredText markups" would convert table in pure reStructuredText syntax. This is the default behavior.

"with HTML tags" would generate table with HTML <TABLE>. This option is useful for those who utilizes the readthedocs.org as a blog system. Please refer to \ |LINK6|\ .

♞ \ |LINK7|\  

.. bottom of content


.. |LINK1| raw:: html

    <a href="http://read-the-docs.readthedocs.io/en/latest/_themes/sphinx_rtd_theme/demo_docs/source/demo.html?highlight=ADMONITION#admonitions" target="_blank">Admonition</a>

.. |LINK2| raw:: html

    <a href="http://docutils.sourceforge.net/docs/ref/rst/directives.html" target="_blank">Directive</a>

.. |LINK3| raw:: html

    <a href="http://www.sphinx-doc.org/en/1.4.8/markup/toctree.html" target="_blank">a sphinx toctree</a>

.. |LINK4| raw:: html

    <a href="https://docs.google.com/document/d/13b5dr8TZoTC5IJZeoiDt066b6mwq67yHqcl4TYUFnk0/edit?usp=sharing" target="_blank">the source document of the index.rst</a>

.. |LINK5| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/ApiDoc.html" target="_blank">How to Create API Docs</a>

.. |LINK6| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/table_in_html.html" target="_blank">this document for details</a>

.. |LINK7| raw:: html

    <a href="https://docs.google.com/document/d/1D2Q53jiQyOoSoqsNhTQuoRb1d2XlIJURgPz2OqrX0DE/edit?usp=sharing" target="_blank">Here is the source document of this page</a>


.. |IMG1| image:: static/User_Guide_1.png
   :height: 192 px
   :width: 536 px

.. |IMG2| image:: static/User_Guide_2.png
   :height: 266 px
   :width: 457 px

.. |IMG3| image:: static/User_Guide_3.png
   :height: 170 px
   :width: 524 px

.. |IMG4| image:: static/User_Guide_4.png
   :height: 205 px
   :width: 281 px

.. |IMG5| image:: static/User_Guide_5.png
   :height: 80 px
   :width: 745 px

.. |IMG6| image:: static/User_Guide_6.png
   :height: 48 px
   :width: 213 px

.. |IMG7| image:: static/User_Guide_7.png
   :height: 156 px
   :width: 458 px

.. |IMG8| image:: static/User_Guide_8.png
   :height: 280 px
   :width: 426 px

.. |IMG9| image:: static/User_Guide_9.png
   :height: 364 px
   :width: 773 px

.. |IMG10| image:: static/User_Guide_10.png
   :height: 130 px
   :width: 140 px

.. |IMG11| image:: static/User_Guide_11.png
   :height: 93 px
   :width: 496 px

.. |IMG12| image:: static/User_Guide_12.png
   :height: 44 px
   :width: 208 px

.. |IMG13| image:: static/User_Guide_13.png
   :height: 90 px
   :width: 753 px

.. |IMG14| image:: static/User_Guide_14.png
   :height: 221 px
   :width: 753 px

.. |IMG15| image:: static/User_Guide_15.png
   :height: 48 px
   :width: 214 px

.. |IMG16| image:: static/User_Guide_16.png
   :height: 140 px
   :width: 1025 px

.. |IMG17| image:: static/User_Guide_17.png
   :height: 46 px
   :width: 200 px

.. |IMG18| image:: static/User_Guide_18.png
   :height: 153 px
   :width: 357 px

.. |IMG19| image:: static/User_Guide_19.png
   :height: 48 px
   :width: 224 px

.. |IMG20| image:: static/User_Guide_20.png
   :height: 133 px
   :width: 266 px

.. |IMG21| image:: static/User_Guide_21.png
   :height: 84 px
   :width: 265 px

.. |IMG22| image:: static/User_Guide_22.png
   :height: 236 px
   :width: 246 px

.. |IMG23| image:: static/User_Guide_23.png
   :height: 545 px
   :width: 664 px

.. |IMG24| image:: static/User_Guide_24.png
   :height: 304 px
   :width: 600 px

.. |IMG25| image:: static/User_Guide_25.png
   :height: 40 px
   :width: 105 px

.. |IMG26| image:: static/User_Guide_26.png
   :height: 52 px
   :width: 152 px

.. |IMG27| image:: static/User_Guide_27.png
   :height: 38 px
   :width: 128 px

.. |IMG28| image:: static/User_Guide_28.png
   :height: 29 px
   :width: 213 px

.. |IMG29| image:: static/User_Guide_29.png
   :height: 165 px
   :width: 746 px

.. |IMG30| image:: static/User_Guide_30.png
   :height: 42 px
   :width: 174 px

.. |IMG31| image:: static/User_Guide_31.png
   :height: 42 px
   :width: 168 px

.. |IMG32| image:: static/User_Guide_32.png
   :height: 36 px
   :width: 186 px

.. |IMG33| image:: static/User_Guide_33.png
   :height: 36 px
   :width: 220 px

.. |IMG34| image:: static/User_Guide_34.png
   :height: 38 px
   :width: 84 px

.. |IMG35| image:: static/User_Guide_35.png
   :height: 40 px
   :width: 148 px

.. |IMG36| image:: static/User_Guide_36.png
   :height: 220 px
   :width: 684 px

.. |IMG37| image:: static/User_Guide_37.png
   :height: 136 px
   :width: 662 px
