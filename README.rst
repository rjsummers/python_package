example_pkg
===========

The purpose of this project is to illustrate the structure and implementation
of a python project, including features such as document generation and unit
testing. This project is using `reStructuredText`_ for document markup.

.. _reStructuredText: https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html

Installation
------------

If the package is registered via. PyPI:

.. code-block:: bash

   pip install example-pkg-rjsummers

If you want to install the project locally and to be able to edit it:

.. code-block:: bash

   pip install -e path/to/ThisProject

Usage
-----

.. code-block:: python

   import example_pkg.arithmetic as arith

   arith.add(2, 2)

..

   4

.. code-block:: python

   arith.subtract(4, 3)

..

   1

.. code-block:: python

   arith.multiply(5, 6)

..

   30

.. code-block:: python

   arith.divide(4, 8)

..

   0.5

Support
-------

If you have any issues with this project, please submit said issue to the
GitHub issue tracker.

Roadmap
-------

Once I get this project's documentation and testing facilities to a
sufficiently advanced stage, this project will probably only be updated as I
become aware of advances in python project management. If you have any
suggestions of how things could be done better, please let me know.

Contributing
------------

This is a rather trivial project in terms of actual capabilities, so I'd be
somewhat surprised if somebody wanted to contribute to this project. If you
want to contribute to this project, please get in contact with me or simply
submit a pull request on GitHub.

Authors and Acknowledgement
---------------------------

This project was developed by me, Randall Summers.

License
-------

This project is licensed under the MIT license. See the LICENSE file for more
details.
