============
Drawing Tool
============


Command line tool that reads drawing instructions from an input file and writes the result in an output file.

Instructions:

- ``C w h``: creates a new canvas of width ``w`` and height ``h``.
- ``L x1 y1 x2 y2``: creates a new line from (``x1``, ``y1``) to (``x2``, ``y2``) using the ``x`` character.
- ``R x1 y1 x2 y2 B x y c``: create a new rectangle, whose upper left corner is (``x1``, ``y1``) and lower right corner is (``x2``, ``y2``) using the ``x`` character.
- ``B x y c``: fills the entire area connected to (``x``, ``y``) with "*colour*" ``c``.

Example input:

.. code-block::

    C 20 4
    L 1 2 6 2
    L 6 3 6 4
    R 16 1 20 3
    B 10 3 o

Expected output:

.. code-block::

    ----------------------
    |                    |
    |                    |
    |                    |
    |                    |
    ----------------------
    ----------------------
    |                    |
    |xxxxxx              |
    |                    |
    |                    |
    ----------------------
    ----------------------
    |                    |
    |xxxxxx              |
    |     x              |
    |     x              |
    ----------------------
    ----------------------
    |               xxxxx|
    |xxxxxx         x   x|
    |     x         xxxxx|
    |     x              |
    ----------------------
    ----------------------
    |oooooooooooooooxxxxx|
    |xxxxxxooooooooox   x|
    |     xoooooooooxxxxx|
    |     xoooooooooooooo|
    ----------------------


Quick start
-----------

Create a `input.txt` file with the drawing instructions:

.. code-block:: bash

    $ cat > ~/input.txt << EOF
    C 20 4
    L 1 2 6 2
    L 6 3 6 4
    R 16 1 20 3
    B 10 3 o
    EOF


.. code-block:: bash

    $ git clone https://github.com/pv8/drawingtool
    $ cd drawingtool
    $ pip install .
    $ drawingtool --input ~/input.txt

*Note*: It's recommended to install inside a virtualenv_.

The result will be written in a `output.txt` file.

It's also possible to output the results to `stdout`:

.. code-block:: bash

    $ drawingtool --input ~/input.txt --stdout

To see all options:

.. code-block:: bash

    $ drawingtool --help


With Docker
~~~~~~~~~~~

If you like Docker_, build the image:

.. code-block:: bash

    $ docker build -t drawingtool .

And run with helper script ``run.sh``:

.. code-block:: bash

    $ ./run.sh drawingtool < input.txt



Development environment
-----------------------

Running tests
~~~~~~~~~~~~~

* With Docker_:

Build the image:

.. code-block:: bash

    $ docker build -t drawingtool .

Then run with the helper script ``run.sh``

.. code-block:: bash

    $ ./run.sh tests

* Without Docker:

Install the development requirements:

.. code-block:: bash

    (drawingtool)$ pip install -r requirements_dev.txt

Then run with pytest_:

.. code-block:: bash

    (drawingtool)$ pytest --cov-report term-missing --cov=.

Debugging
~~~~~~~~~

Include the ipdb_ breakpoint (``import ipdb; ipdb.set_trace()``) and run:

* With Docker:

.. code-block:: bash

    $ ./run.sh tests

* Without Docker:

.. code-block:: bash

    $ (drawingtool)$ pytest -s

Linting
~~~~~~~

* With Docker:

.. code-block:: bash

    $ ./run.sh pep8

* Without Docker:

.. code-block:: bash

    $ (drawingtool)$ flake8 --statistics .


.. _`Python 3`: https://www.python.org/downloads/release/python-364/
.. _Docker: https://docs.docker.com/install/
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _pytest: https://docs.pytest.org/en/latest/
.. _ipdb: https://github.com/gotcha/ipdb


License
-------

MIT
