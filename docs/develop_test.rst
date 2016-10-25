
GGeditor
########

Paragraphs
**********

A paragraph with hypertext: **GGeditor :sup:`1.0`** is a  `Google Docs Add\-on <https://support.google.com/a/answer/4530135?hl=en>`_  for editing reST file. That is, you edit *V :sub:`2`* the content in Google Docs and with GGeditor to convert it into  `reST format <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_ . 

Secondary paragraph: The converted reST file can be downloaded or committed to Github. Once it was in the Github, it will be integrated with the sphinx service by `Read The Docs <https://readthedocs.org/>`_ .

   Indent paragraph: The converted reST file can be downloaded or committed to Github. Once it was in the Github, it will be integrated with the sphinx service by `Read The Docs <https://readthedocs.org/>`_ .

      Secondary indent paragraph: The converted reST file can be downloaded or committed to Github. Once it was in the Github, it will be integrated with the sphinx service by `Read The Docs <https://readthedocs.org/>`_ .

      Another secondary indent paragraph: The converted reST file can be downloaded or committed to Github. Once it was in the Github, it will be integrated with the sphinx service by `Read The Docs <https://readthedocs.org/>`_ .

Numbered List:
**************

#. Easy start for reST beginners.

#. Almost what you see is what you get.

#. Preview generated reST files and download it.

#. nested with number list

   #. secondary numbered list

   #. another item

#. Just copy and paste images, the reST Editor will handle them.

List with nested list
*********************

* When repository was renamed:

   * If the repository or folder name of the binding file in Github was renamed, a re\-binding is required for committing.

* Open hyperlink in a new tab:

   * This is not supported.  `Please see details here <https://github.com/sphinx-doc/sphinx/issues/1634>`_ .

* Only text is allowed in a list item. Text with hyperlink is fine.

   * But image, table in a list item is not supported. If it does, it will be interpreted as outside the list.

Table
*****


+---------------------------+-----------------------------------------------------+
|Header 1A                  |Header 1B                                            |
+===========================+=====================================================+
|Header 2A                  |Header 2B                                            |
+---------------------------+-----------------------------------------------------+
|Cell with text             |Cell with link to  `google <http://www.google.com>`_ |
+---------------------------+-----------------------------------------------------+
|nested table, not supported|image in cell, not supported                         |
|a                          |                                                     |
|b                          |                                                     |
|d                          |                                                     |
|c                          |                                                     |
|                           |                                                     |
+---------------------------+-----------------------------------------------------+


+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------------------+
|Header                                                                                                                    |Text                                                |In Bold Style        |
+==========================================================================================================================+====================================================+=====================+
|Normal cell text                                                                                                          |                                                    |Empty cell in my left|
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------------------+
|Hyper link is fine                                                                                                        |Link to  `google <http://www.google.com>`_          |                     |
|                                                                                                                          |This line Link to  `FB <http://www.facebook.com>`_  |                     |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------------------+
|Image, list were not exported, Image, list were not exported, Image, list were not exported, Image, list were not exported|This is line 1                                      |At the end           |
|                                                                                                                          |                                                    |                     |
|                                                                                                                          |This is line 2                                      |                     |
|                                                                                                                          |                                                    |                     |
|                                                                                                                          |This is line 3                                      |                     |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+---------------------+


+---------+------------------------------------------------------+
|Like this|                                                      |
+---------+------------------------------------------------------+
|         |a like to  `google <http://www.google.com>`_  <\- link|
+---------+------------------------------------------------------+
