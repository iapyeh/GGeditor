\ **GGEditor Development**\ 

* \ `Link`_\  to the GGeditor documentation in the readthedocs.org
* \ `Link`_\  to the GGeditor documentation in the Github
* \ `Link`_\  to the User Guide of the GGeditor (Lots of usage example)


.. Hint:: 

    If you manually put a substitution markup, you got to provide the replacement markup manu. The above table is generated from the content below:\ |IMG1|\ 


.. code:: 

    var body = DocumentApp.getActiveDocument().getBody();
    
     // Create a two-dimensional array containing the cell contents.
     var cells = [
       ['Row 1, Cell 1', 'Row 1, Cell 2'],
       ['Row 2, Cell 1', 'Row 2, Cell 2']
     ];
    
     // Build a table from the array.
     body.appendTable(cells);
    
    



.. _`Link`: https://docs.google.com/document/d/1D2Q53jiQyOoSoqsNhTQuoRb1d2XlIJURgPz2OqrX0DE/edit?usp=sharing

.. |IMG1| image:: static/develop_test_1.png
   :height: 224 px
   :width: 522 px
