
.. _h7f551d34286643173b507b745668a4f:

How-to the Readthedocs
**********************

This is a simple guideline to help GGeditor users to setup a basic project of the \ `readthedocs.org`_\ . I have no idea if this is the best practice, it just works for me.

#. You got to have a index.rst in the “docs” folder
#. You got to insert markups of “toctree” table in the index.rst.
#. You got to have a conf.py in the “docs” folder.
#. You got to have a file named “theme_overrides.css” in the “docs/static” folder.

That’s all. With the above 4 steps, you can go readthedocs.org  and create a project for your repository.

.. _h341e5179157a606f5e6b5f5570287f2c:

Step 1: create the docs/index.rst
=================================

If the “docs” folder does not exist in your Github repository, you can create the docs/index.rst directly by binding to “docs/index.rst” in the dialog of “New File”.

\ |IMG1|\ 

\ |IMG2|\ 

.. _h195ff4c157e501d115f391d4e173b36:

Step 2: insert toctree markup to the index.rst
==============================================

The index.rst is the homepage of your project in the readthedocs.org. You can put anything you want. But you should not miss the awesome feature - the sidebar of “table of contents” for your documentation. Just simply do this in the GGeditor markup panel:

#. Insert a “Table of Contents” from the “GGeditor Markup Panel / Markup / Directives”

\ |IMG3|\ 

Then, the document would have a “toctree” table like this:

\ |IMG4|\ 

.. _h7f1657c7763721b311b652230436640:

Step 3: conf.py
===============

The Github allows user to create a new file in the repository page:

\ |IMG5|\ 

Then input the path and filename for your new file (docs/conf.py).

\ |IMG6|\ 

Below is the context for you to copy and paste.

.. code:: python

    # -*- coding: utf-8 -*-
    
    from __future__ import unicode_literals
    import sys, os
    
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    
    sys.path.append(os.path.abspath(os.pardir))
    
    __version__ = '1.0'
    
    # -- General configuration -----------------------------------------------------
    source_suffix = '.rst'
    master_doc = 'index'
    project = 'CHANGE-THIS'
    copyright = '2016, CHANGE-THIS'
    # The name of the Pygments (syntax highlighting) style to use.
    pygments_style = 'sphinx'
    
    extlinks = {}
    
    # -- Options for HTML output ---------------------------------------------------
    
    html_theme = 'default'
    
    html_static_path = ['static']
    
    def setup(app):
        # overrides for wide tables in RTD theme
        app.add_stylesheet('theme_overrides.css') # path relative to static

.. _h4a47434f5c5745347cc5f1b4d2d5023:

Step 4: theme_overrides.css
===========================

You can use the same way to create a new “theme_overrides.css” in the “docs/static” folder. Like this:

\ |IMG7|\ 

Below is the content of the theme_overrides.css for you to copy and paste.

.. code:: 

    .wy-table-responsive table td, .wy-table-responsive table th {
       white-space: inherit;
    }

Because the standard theme set the white-space to be “no-wrap” for table cell. Which is not desirable for the converted table of the GGeditor.

.. Note:: 

    Github has tool which can create plain text file (such as conf.py and Theme_overrides.css) very easily.

You can reference \ `the index.rst of the GGeditor`_\  for example.



.. _`readthedocs.org`: https://readthedocs.org
.. _`the index.rst of the GGeditor`: https://docs.google.com/document/d/13b5dr8TZoTC5IJZeoiDt066b6mwq67yHqcl4TYUFnk0/edit?usp=sharing

.. |IMG1| image:: static/how2Readthedocs_1.png
   :height: 434 px
   :width: 524 px

.. |IMG2| image:: static/how2Readthedocs_2.png
   :height: 396 px
   :width: 664 px

.. |IMG3| image:: static/how2Readthedocs_3.png
   :height: 493 px
   :width: 310 px

.. |IMG4| image:: static/how2Readthedocs_4.png
   :height: 478 px
   :width: 810 px

.. |IMG5| image:: static/how2Readthedocs_5.png
   :height: 218 px
   :width: 1025 px

.. |IMG6| image:: static/how2Readthedocs_6.png
   :height: 149 px
   :width: 418 px

.. |IMG7| image:: static/how2Readthedocs_7.png
   :height: 149 px
   :width: 626 px
