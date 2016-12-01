
.. _h61d62117b185b142af77803e484226:

How to Create API Docs
**********************

.. _h7e6c19301b527f27134346047387722:

Manually
========

.. _h745e1e562295d71429135181e4a5c:

1. Write Inline Document
------------------------

\ |LINK1|\ 

.. _h1d755b425f387a13327793f2f664e:

2. Create API Docs for a Python script
--------------------------------------

Support we are going to create the document for script "backend/apidocsample.py"

.. _h973462d7b46a1e2d193f3a23774ab:

Modify conf.py
~~~~~~~~~~~~~~

in the "docs/conf.py"\ [#F1]_\ , 

#. append a line to insert the backend to sys.path
#. ensure the autodoc and napoleon are in the extensions


.. code:: python

    import sys, os
    
    # append the next line to conf.py
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','backend'))
    
    # ensure the autodoc and napoleon are in the extensions
    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

.. _h4d2033204b2247687d5f365f20731441:

Create apidocsample.rst
~~~~~~~~~~~~~~~~~~~~~~~

Create the  apidocsample.rst in the "docs"

.. code:: 

    apidocsample module
    ====================
    
    .. automodule:: apidocsample
        :members:
        :undoc-members:
        :show-inheritance:

.. _h732845536db30978122116f26674:

3. Done
-------

That's all. Then you can see the api document at readthedocs.org by this URL:

http://<project-name>.readthedocs.io/en/latest/apidocsample.html


.. |LINK1| raw:: html

    <a href="http://google.github.io/styleguide/pyguide.html" target="_blank">Google Python Style Guide</a>



.. rubric:: Footnotes

.. [#f1]  More on http://www.sphinx-doc.org/en/1.4.8/config.html#build-config
