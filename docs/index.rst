
.. _h28105e656d4d48041184d771d3b4a1a:

GGeditor
########


.. toctree:: 
    :maxdepth: 2

    DocStructure
    Examples
    how2Readthedocs
    Limitations
    Sponsors
    User Guide

\ **GGeditor**\  is a Google Docs Add-on for generating \ `reStructuredText`_\  file from the Google Docs. The generated reST file can be committed to the Github repository with the GGeditor. Then, that repository’s documentations hosted by the \ `Read The Docs`_\  got automatically updated.

\ |IMG1|\ 


.. Hint:: 

    You don’t need to trigger conversion before committing and downloading, the committing and downloading would do conversion at first.

.. _h6897050511836763421463e2b4b685:

Features
********

#. Easy starting for reST beginners, even no idea about reST markups.
#. Powered by the Google Docs. Almost what you see is what you get.
#. One-click to commit to the Github repository.
#. Preview the generated reST file and download to local machine.
#. Support headings, bold, italic, hyperlink, subscript and superscript.
#. Support footnotes, image, list item and table.
#. Support full-width characters (CKJ) in headings and table.
#. Support internal links to bookmarks, headings and Google Docs native table of contents (in document table of contents).
#. Support cross-document table of content (.. doctree::) for the readthedocs.org.
#. Support admonitions of the readthedocs.org.

.. _h131f586a50795a4822677d4166231766:

How to install
**************

#. Open a Google Docs document.
#. On the menu item “Add-ons”, click the “Get Add-ons”
#. In the search box, input “GGeditor”, then click on the GGeditor icon to install.

\ |IMG2|\ 

.. _h84e3b4616757118376d336e2e5d5d23:

For reStructuredText Beginners
******************************

I guess that  you might feel a little bit of confusing if you just started your journey on reStructuredText. I wrote a chapter for you to help your documentation task to be quickly completed like the GGeditor. I spent over 2 months to tackle it. Now you have the GGeditor and this how-to chapter, You might accomplish it in several hours.

.. _h59e47f2a4a50742f566e3f654a4648:

Related Works
*************

* \ `Gitbook`_\ : it has a markup editor
* \ `Online reStructuredText editor`_\ 

.. _h7c12a2e595c631221f363d4e55c21:

Acknowledgments
***************

* Andrey Rublev as well as \ `all the contributors`_\  of the \ `Online reStructuredText editor`_\ , it is a great tool for beginner to learn the reST markups.
* \ `Readthedocs.org`_\ , it provides a great service, which encourage me to create the GGeditor.
* Philip Schatz as well as \ `all the contributors`_\  of the  \ `octokat.js`_\  project. The Github-related implementation is based on their great works.
* Bitwiseshiftleft as well as \ `all the contributors`_\  of the \ `sjcl`_\  projects. The sjcl.js is used for credentials encryption.

\ `Source document in the Google Docs`_\ 

.. _`reStructuredText`: https://en.wikipedia.org/wiki/ReStructuredText
.. _`Read The Docs`: https://readthedocs.org/
.. _`Gitbook`: https://www.gitbook.com
.. _`Online reStructuredText editor`: http://rst.ninjs.org/
.. _`all the contributors`: https://github.com/bitwiseshiftleft/sjcl/graphs/contributors
.. _`Readthedocs.org`: https://readthedocs.org
.. _`octokat.js`: https://github.com/philschatz/octokat.js
.. _`sjcl`: https://github.com/bitwiseshiftleft/sjcl
.. _`Source document in the Google Docs`: https://docs.google.com/document/d/13b5dr8TZoTC5IJZeoiDt066b6mwq67yHqcl4TYUFnk0/edit?usp=sharing

.. |IMG1| image:: index/index_1.png
   :height: 250 px
   :width: 504 px

.. |IMG2| image:: index/index_2.png
   :height: 213 px
   :width: 326 px
