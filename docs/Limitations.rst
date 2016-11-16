
.. _h1a461f6b1275321a16291dd169a6c:

Limitations
###########

.. _h19176e602c6c3f6828a7e207b523e9:

Unsupported Google Docs Features:
*********************************

The Google Docs is a powerful editor, but not all features are supported to convert to reST markups. Below is the list (included but not limited to)

* Comments. This is not supported by the reST.
* Drawing objects. Because there is no API to get it as an image.
* List styles. The list style is defined by the CSS settings in the html page.
* Math equations. Because this is no API to get it as an image.
* Multi\-columns. This is not supported by the reST.
* Page break. This is not able to apply to a html page.
* Page header and page footer. This is not supported by the reST.
* Page numbering. This is not able to apply to a html page.

.. _h65776f3b486b79192426655c476e97b:

Known Issues:
*************

.. _h523d4e2aa4a407c262263331325295e:

reST related
============

* Open hyperlink in a new tab:

    * This is not supported. \ `Please see details here`_\ .

* Table in a list item is not supported. It will be converted to a stand\-alone table.
* Nested table in a table cell is not supported.

.. _h69271f6b544a4942467e713a34332e47:

Github related
==============

* When repository was renamed:

    * If the repository or folder name of the binding file in Github was renamed, a re\-binding is required for committing.

* When the binding file has changed

    * If the binding file has changed, according to the new binding name, a new  image subfolder might be created. Which means the original image subfolder should be removed manually.

.. _h1851781a7781866c373d74142e52a:

Image subfolder naming scheme
*****************************

* If there is an image in a Google Docs document which is binding to README.rst, when committing to the Github, that image will be put into a subfolder named “README”. 
* Which means if there is a file named “README” in the same folder of README.rst, confliction would happen.


.. _`Please see details here`: https://github.com/sphinx-doc/sphinx/issues/1634
