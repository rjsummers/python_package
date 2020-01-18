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
