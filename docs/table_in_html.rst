
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


|REPLACE1|

.. _hf5e23482d7d5f257f501e131f189d:

List items
----------


|REPLACE2|

.. _h2929565b25e3945d5f2b58e2a37:

List items 2
------------


|REPLACE3|

.. _bookmark-kix-q74pjka91gr0:

.. _h60543071b22465442566921864d10:

col and row span
----------------


|REPLACE4|

.. _h2c1d74277104e41780968148427e:




.. _h1a461f6b1275321a16291dd169a6c:

Limitations
===========

* Horizental alignment is not supported. Because of the Doc's API always returns null when getting this attribute value.(API issue)

* Constant font style (font-size, family) in a single cell.

* Vertial-alignment of cell content. (API issue)

* Cell height (API isue)

♞ \ |LINK1|\ 

.. bottom of content


.. |REPLACE1| raw:: html

    <table cellspacing="0" cellpadding="0" style="width:75%">
    <tbody>
    <tr><td style="width:67%;background-color:#ff9900;vertical-align:Center;border:solid 3px #4a86e8"><p>green background with content of italic, bold and 有中文內容及上下標 </p><p style="font-size:10px"><p><span  style="font-size:10px">x<sup>2</sup>+y<sup>2</sup>+T<sub>ab</sub></span></p></td><td style="width:33%;color:#0000ff;vertical-align:Top;border:solid 3px #4a86e8"><p style="color:#0000ff;font-size:14px;font-family:Comic Sans MS"><span  style="color:#0000ff;font-size:14px;font-family:Comic Sans MS">words in blue with font-family "Comic Sans MS"</span></p></td></tr>
    </tbody></table>

.. |REPLACE2| raw:: html

    <table cellspacing="0" cellpadding="0" style="width:75%">
    <tbody>
    <tr><td style="width:67%;vertical-align:Top;border:solid 3px #ff0000"><ol style="list-style:decimal;list-style-image:inherit;padding:0px 40px;margin:initial"><li style="list-style:inherit;list-style-image:inherit"><span  style="font-size:14px">external <a href="http://www.google.com" target="_blank">google</a> </span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="font-size:14px">bookmark <a href="#bookmark-kix-q74pjka91gr0">link</a> </span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="font-size:14px">cross-reference <a href="Examples.html">Examples</a> </span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#333333;font-size:14px"><span style="font-style:italic">italic</span> text item</span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#333333;font-size:14px"><span style="font-weight:bold">bold</span> text item</span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#4a86e8;font-size:14px">this is</span><img src="_images/table_in_html_2.png" style="width:45px;height:41px;vertical-align: baseline;"><span  style="color:#4a86e8;font-size:14px">item with image</span></li></ol></td><td style="width:33%;background-color:#00ff00;vertical-align:Top;border:solid 3px #ff0000"><p>green background with content of <span style="font-style:italic">italic</span>, <span style="font-weight:bold">bold</span> and 有中文內容及上下標x<sup>2</sup>+y<sup>2</sup>+T<sub>ab</sub></p></td></tr>
    </tbody></table>

.. |REPLACE3| raw:: html

    <table cellspacing="0" cellpadding="0" style="width:100%">
    <tbody>
    <tr><td style="background-color:#ffff00;vertical-align:Top;border:solid 3px #0000ff"><p style="color:#333333;font-size:14px"><span  style="color:#333333;font-size:14px">this is a list</span></p><ol style="list-style:decimal;list-style-image:inherit;padding:0px 40px;margin:initial"><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#333333;font-size:14px">this is 1</span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#333333;font-size:14px">this is 2</span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#333333;font-size:14px">this is 3</span></li></ol><p style="color:#333333;font-size:14px"><span  style="color:#333333;font-size:14px">this has image in cell</span></p><p style="font-size:14px"><a href="http://www.google.com" target="_blank"><img src="_images/table_in_html_2.png" style="width:69px;height:62px;vertical-align: baseline;"></a></p></td><td style="background-color:#00ff00;vertical-align:Top;border:solid 3px #0000ff"><p style="color:#333333;font-size:14px"><span  style="color:#333333;font-size:14px">this is a list</span></p><ul style="list-style:disc;list-style-image:inherit;padding:0px 40px;margin:initial"><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#4a86e8;font-size:14px">this is</span><a href="http://www.google.com" target="_blank"><img src="_images/table_in_html_2.png" style="width:41px;height:37px;vertical-align: baseline;"></a><span  style="color:#4a86e8;font-size:14px"> item with image</span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="color:#ff0000;font-size:14px">this is item in red</span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="font-size:14px">this is italic item<a href="http://www.google.com" target="_blank"> link to google</a></span></li><li style="list-style:inherit;list-style-image:inherit"><span  style="font-size:14px">this is <span style="font-weight:bold">bold</span> item link to <a href="Examples.html">Example.html</a></span></li></ul></td></tr>
    </tbody></table>

.. |REPLACE4| raw:: html

    <table cellspacing="0" cellpadding="0" style="width:85%">
    <thead>
    <tr><th style="text-align:center;width:16%;background-color:#666666;color:#333333;vertical-align:Top;border:solid 1px #000000"><p style="color:#333333;font-size:10px;margin-bottom:23"><span  style="color:#333333;font-size:10px">Header</span></p></th><th style="text-align:center;width:21%;background-color:#f3f3f3;color:#333333;vertical-align:Top;border:solid 1px #000000"><p style="color:#333333;font-size:10px;margin-bottom:23"><span  style="color:#333333;font-size:10px">Header</span></p></th><th style="text-align:center;width:21%;background-color:#93c47d;color:#333333;vertical-align:Top;border:solid 1px #000000"><p style="color:#333333;font-size:10px;margin-bottom:23"><span  style="color:#333333;font-size:10px">Header</span></p></th><th style="text-align:center;width:21%;background-color:#c27ba0;color:#333333;vertical-align:Top;border:solid 1px #000000"><p style="color:#333333;font-size:10px;margin-bottom:23"><span  style="color:#333333;font-size:10px">Header</span></p></th><th style="text-align:center;width:21%;background-color:#6d9eeb;color:#333333;vertical-align:Top;border:solid 1px #000000"><p style="color:#333333;font-size:10px;margin-bottom:23"><span  style="color:#333333;font-size:10px">Header</span></p></th></tr>
    </thead><tbody>
    <tr><td style="vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td colspan="5" style="background-color:#ffff00;vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td rowspan="2" colspan="2" style="background-color:#4a86e8;vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><img src="_images/table_in_html_2.png" style="width:80px;height:73px;vertical-align: baseline;"></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td rowspan="3" style="background-color:#00ff00;vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><img src="_images/table_in_html_2.png" style="width:77px;height:72px;vertical-align: baseline;"></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td rowspan="3" style="background-color:#ff0000;vertical-align:Top;border:solid 1px #000000"><p style="margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td rowspan="2" style="background-color:#4a86e8;vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td rowspan="2" colspan="2" style="background-color:#00ff00;vertical-align:Center;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text and </span><a href="http://www.google.com" target="_blank"><img src="_images/table_in_html_2.png" style="width:74px;height:68px;vertical-align: baseline;"></a></p></td><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td style="vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td><td colspan="4" style="vertical-align:Top;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    <tr><td colspan="5" style="background-color:#ffff00;vertical-align:Bottom;border:solid 1px #000000"><p style="font-size:10px;margin-bottom:23"><span  style="font-size:10px">Text</span></p></td></tr>
    </tbody></table>


.. |LINK1| raw:: html

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
