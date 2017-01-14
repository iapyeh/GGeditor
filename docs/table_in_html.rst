
.. _h7417311651356b38234173e38352a34:

Table conversion with HTML
**************************

Table conversion to reStructuredText has limitation due to limited features were supported by the reStructuredText. For example, row-span, column-span and background color were not supported in reStructuredText.

This could be a problem for users who want to write their blogs in reStructuredText. The GGeditor solves this issue by converting a table to HTML-table instead of the reStructuredText-table.

.. _h5e3c71275653e247c4d305d12131433:

Supported Features
==================

* Columns width in propotion of percentage.

* Column span or row span.

* Cell background and foreground color.

* Table border and cell border.

* Cell-level font-size

.. _h23786b7a28397e315b4726412e52451:

Eenable this feature
====================

Converting table with HTML is not default behavior. To enable it, please open the Settings dialog to enable it.

\ |IMG1|\ 

.. _h17cf336a3119355a1c01f75426961:

Examples
========

.. _h365645603e234c6a6a291b1b7e1d534:

Background, Foreground and links
--------------------------------


+---------------------------------------------------------------------+----------------------------------------------+
|green background with content of italic, bold and 有中文內容及上下標 |words in blue with font-family "Comic Sans MS"|
|                                                                     |                                              |
|x\ |STYLE0|\ +y\ |STYLE1|\ +T\ |STYLE2|\                             |                                              |
+---------------------------------------------------------------------+----------------------------------------------+

.. _hf5e23482d7d5f257f501e131f189d:

List items
----------


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
|#. external \ |LINK1|\             |green background with content of \ |STYLE5|\ , \ |STYLE6|\  and 有中文內容及上下標x\ |STYLE7|\ +y\ |STYLE8|\ +T\ |STYLE9|\ |
|                                   |                                                                                                                           |
|#. bookmark \ |LINK2|\             |                                                                                                                           |
|                                   |                                                                                                                           |
|#. cross-reference \ |LINK3|\      |                                                                                                                           |
|                                   |                                                                                                                           |
|#. \ |STYLE3|\  text item          |                                                                                                                           |
|                                   |                                                                                                                           |
|#. \ |STYLE4|\  text item          |                                                                                                                           |
|                                   |                                                                                                                           |
|#. this is\ |IMG2|\ item with image|                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _h2929565b25e3945d5f2b58e2a37:

List items 2
------------


+----------------------+------------------------------------------------+
|this is a list        |this is a list                                  |
|                      |                                                |
|#. this is 1          |* this is\ |IMG4|\  item with image             |
|                      |                                                |
|#. this is 2          |* this is item in red                           |
|                      |                                                |
|#. this is 3          |* this is italic item \ |LINK4|\                |
|                      |                                                |
|this has image in cell|* this is \ |STYLE10|\  item link to \ |LINK5|\ |
|                      |                                                |
|\ |IMG3|\             |                                                |
+----------------------+------------------------------------------------+

.. _bookmark-kix-q74pjka91gr0:

.. _h60543071b22465442566921864d10:

col and row span
----------------


+------+----------+-------------------+----------+------+
|Header|Header    |Header             |Header    |Header|
+======+==========+===================+==========+======+
|Text  |Text      |Text               |Text      |Text  |
+------+----------+-------------------+----------+------+
|Text  |          |                   |          |      |
+------+----------+-------------------+----------+------+
|Text  |Text      |Text               |Text      |Text  |
+------+----------+-------------------+----------+------+
|Text  |Text      |Text               |\ |IMG5|\ |      |
+------+----------+-------------------+----------+------+
|Text  |Text      |Text               |          |      |
+------+----------+-------------------+----------+------+
|Text  |\ |IMG6|\ |Text               |Text      |Text  |
+------+----------+-------------------+----------+------+
|Text  |          |Text               |          |Text  |
+------+----------+-------------------+----------+------+
|Text  |          |Text               |          |Text  |
+------+----------+-------------------+----------+------+
|      |Text      |Text and \ |IMG7|\ |          |Text  |
+------+----------+-------------------+----------+------+
|Text  |Text      |                   |          |Text  |
+------+----------+-------------------+----------+------+
|Text  |Text      |                   |          |      |
+------+----------+-------------------+----------+------+
|Text  |          |                   |          |      |
+------+----------+-------------------+----------+------+

.. _h2c1d74277104e41780968148427e:




.. _h1a461f6b1275321a16291dd169a6c:

Limitations
===========

* Horizental alignment is not supported. Because of the Doc's API always returns null when getting this attribute value.(API issue)

* Constant font style (font-size, family) in a single cell.

* Vertial-alignment of cell content. (API issue)

* Cell height (API isue)

♞ \ |LINK6|\ 

.. bottom of content


.. |STYLE0| replace:: :sup:`2`

.. |STYLE1| replace:: :sup:`2`

.. |STYLE2| replace:: :sub:`ab`

.. |STYLE3| replace:: *italic*

.. |STYLE4| replace:: **bold**

.. |STYLE5| replace:: *italic*

.. |STYLE6| replace:: **bold**

.. |STYLE7| replace:: :sup:`2`

.. |STYLE8| replace:: :sup:`2`

.. |STYLE9| replace:: :sub:`ab`

.. |STYLE10| replace:: **bold**


.. |LINK1| raw:: html

    <a href="http://www.google.com" target="_blank">google</a>

.. |LINK2| raw:: html

    <a href="#bookmark-kix-q74pjka91gr0">link</a>

.. |LINK3| raw:: html

    <a href="Examples.html">Examples</a>

.. |LINK4| raw:: html

    <a href="http://www.google.com" target="_blank">link to google</a>

.. |LINK5| raw:: html

    <a href="Examples.html">Example.html</a>

.. |LINK6| raw:: html

    <a href="https://docs.google.com/document/d/1d-NgzTw418Ml3PgQPLoJaw76whgnUW2x1IUt8WjOrnI/edit?usp=sharing" target="_blank">Source document of this page</a>


.. |IMG1| image:: static/table_in_html_1.png
   :height: 165 px
   :width: 566 px

.. |IMG2| image:: static/table_in_html_2.png
   :height: 41 px
   :width: 45 px

.. |IMG3| image:: static/table_in_html_2.png
   :height: 62 px
   :width: 69 px
   :target: http://www.google.com

.. |IMG4| image:: static/table_in_html_2.png
   :height: 37 px
   :width: 41 px
   :target: http://www.google.com

.. |IMG5| image:: static/table_in_html_2.png
   :height: 73 px
   :width: 80 px

.. |IMG6| image:: static/table_in_html_2.png
   :height: 72 px
   :width: 77 px

.. |IMG7| image:: static/table_in_html_2.png
   :height: 68 px
   :width: 74 px
   :target: http://www.google.com
