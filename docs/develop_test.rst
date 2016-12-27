
.. _h2c1d74277104e41780968148427e:




.. _h2c1d74277104e41780968148427e:




.. _hc446611b54b3080663873375a615b:

Test
####

\ |IMG1|\ 

|REPLACE1|

\ |LINK1|\ 只是一個應用程式，要有人學習如何使用，還要安裝、執行，然後還要架一個網站把它產生的HTML檔案及附圖放上去。幸好，Sphinx只要用pip安裝就可以輕鬆完成。比較大的困擾是，如果不是資源豐沛的公司，要架設網站是挺耗時費力的，頻寬、網址申請、VM管理還有惱人的資安問題要有對策。如果這件事情有人代勞，而且免費，那該多好？如果你也有這樣的問題，那麼\ |LINK2|\  (RTD)跟Github就能幫助你。

\ |STYLE0|\ ，\*\*RTD的\*\*後台就可以從你的Github repository中用Sphinx產生你的系統文件，而且還能全文檢索。也就是說，RTD是一個hosting技術文件的網站。它是免費的\ [#F1]_\ 。使RTD跟Github之後，文件的架構就會變成這樣：


..  Danger:: 

    (content of Danger)


.. admonition:: Release Note

    (content of Change-me)

.. _h2c1d74277104e41780968148427e:





.. admonition:: Dec 12, 2012

    Improved:
    
    * Create new file in github failed if the new path has new folder great than 1 level, ex, create docs/blog/technical/how2pythondocs.py in docs/ where blog/technical is not existed yet
    
    * For In-document TOC, there is no extra empty line between items.
    
    * For partial convsion of selection or table, the conversion dialog would break a line for every 60 characters. It makes content easier to read.
    
    * For simplicity, the “Download” button is hidden in partial conversion except images are included.
    
    * Hyperlink in footnote content is allowed.
    
    * “Add link to another document” only displays items binding to the same repository with current document.And generated path is relative to current document.
    
    
    Fixed:
    
    #. Insert link to another document failed for binded documents if binding path is different document path
    
    Featured:
    
    * Add custom admonition. No more markup, just title it.\ |IMG2|\ 
    
    Limited:
    
    * Internal link to heading does not work. Currently there is no API to identifiy the target heading element. Please use “Bookmark“ instead.

.. _h2c1d74277104e41780968148427e:




.. _bookmark-id-c2rvbdk5c3xc:

.. _h3f12453542177d82f2d5e35105a7a44:

Changes
=======

#. (improvement) Create new file in github failed if the new path has new folder great than 1 level, ex, create docs/blog/technical/how2pythondocs.py in docs/ where blog/technical is not existed yet

#. (bugfixing) Insert link to another document failed for binded documents if binding path is different document path

#. (limitation) Internal link to heading does not work. Currently there is no API to identifiy the target heading element. Please use “Bookmark“ instead.

#. (feature) Add custom admonition template

#. (improvement) For In-document TOC, there is no extra empty line between items.


.. bottom of content


.. |STYLE0| replace:: **你把文件commit到Github去**


.. |REPLACE1| raw:: html

            <table id="calculator">
            <tr><th>月薪</th></tr>
            <tr><td><input class="field" type="number" id="salary" value="36000"></td></tr>
            <tr><th>類型</th></tr>
            <tr><td><select class="field" id="type">
                <option value="1" selected>工作日</option>
                <option value="2">休息日</option>
                <option value="3">例假日</option>
                <option value="4">特休</option>
                <option value="5">國定假日</option>
                </select></td></tr>
            <tr><th>上班時間</th></tr>
            </table>
    

.. |LINK1| raw:: html

    <a href="#bookmark-id-c2rvbdk5c3xc">Sphinx</a>

.. |LINK2| raw:: html

    <a href="https://readthedocs.org" target="_blank">readthedocs.org</a>



.. rubric:: Footnotes

.. [#f1]  Hosting的部分主要是由佛心來的 `Rockspace <https://www.rackspace.com>`__ 買單。

.. |IMG1| image:: static/develop_test_1.png
   :height: 94 px
   :width: 82 px

.. |IMG2| image:: static/develop_test_2.png
   :height: 114 px
   :width: 400 px
