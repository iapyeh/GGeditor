
.. _h785738613d761e607465672148487a7e:

Limit\ |STYLE0|\ \ |IMG1|\ \ |LINK1|\ 獨\ [#F1]_\ \ |STYLE1|\ 
##############################################################

.. _h19176e602c6c3f6828a7e207b523e9:

Unsupported Google Docs Features:
*********************************

The Google Docs is a powerful editor, but not all features are supported to convert to re\ |STYLE2|\  markups. Be\ |STYLE3|\  is the list (included but not limited to)

* Comments. This is not supported by the reST.
* Drawing objects. Because there is no API to get it as an image.
* List styles. The list style is defined by the CSS settings in the html page.
* Math \ |STYLE4|\ . Because this is no API to get it as an image.
* \ |STYLE5|\ . This is not supported by the reST.
* Page break.\ |STYLE6|\  to apply to a html page.
* Page header and page footer. \ |STYLE7|\  by the reST.
* Page numbering. This is not able to apply to a html page.

.. _h65776f3b486b79192426655c476e97b:

Known Issues:
*************

.. _h1f753e737333503f6591234143cc4:

reStructuredText related
========================

* Table in a list item is not supported. It will be converted to a stand-alone table.
* Nested table in a table cell is not supported.
* Video is not supported. The Google Docs does not allow to embed videos neither.

.. _h69271f6b544a4942467e713a34332e47:

Github related
==============

* When repository was renamed:

    * If the repository or folder name of the binding file in Github was renamed, a re-binding is required for committing.

* When the binding file has changed

    * If the binding file has changed, according to the new binding name, a new  image subfolder might be created. Which means the original image subfolder should be removed manually.


.. |STYLE0| replace:: :sup:`ations`

.. |STYLE1| replace:: :sub:`立`

.. |STYLE2| replace:: :sup:`ST`

.. |STYLE3| replace:: :sub:`low`

.. |STYLE4| replace:: **equations**

.. |STYLE5| replace:: **Multi-columns**

.. |STYLE6| replace:: *This is not able*

.. |STYLE7| replace:: *This is not supported*


.. |LINK1| raw:: html

    <a href="http://www.google.com" target="_blank">台灣</a>



.. rubric:: Footnotes

.. [#f1]  Taiwan independence

.. |IMG1| image:: static/Limitations_1.png
   :height: 181 px
   :width: 181 px
