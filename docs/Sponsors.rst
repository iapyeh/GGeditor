
.. _h187f5346c53211d23322593d555927:

Sponsors
########

.. _h39333d6c6e523d6d25172c215019258:

Neusauber.com
*************

IIS, Academia Sinica

.. hint::

    ``p PORTMASK`\`: A hexadecimal bitmask of the ports to configure
    ``q NQ`\`: A number of queues (=ports) per lcore (default is 1)
    ``K PERIOD`\`: Heartbeat check period in ms(5ms default; 86400 max)
    ``T PERIOD`\`: statistics will be refreshed each PERIOD seconds (0 to disable, 10 default, 86400 maximum).

To run the application in linuxapp environment with 4 lcores, 16 ports 8 RX queues per lcore and a ping interval of 10ms, issue the command:


.. code::

    ./build/l2fwd\-keepalive \-c f \-n 4 \-\- \-q 8 \-p ffff \-K 10


.. danger::

    ./build/l2fwd\-keepalive \-c f \-n 4 \-\- \-q 8 \-p ffff \-K 10

./build/l2fwd\-keepalive \-c f \-n 4 \-\- \-q 8 \-p ffff \-K 10
