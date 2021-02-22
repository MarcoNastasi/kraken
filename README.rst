======
kraken
======


.. image:: https://img.shields.io/pypi/v/kraken.svg
        :target: https://pypi.python.org/pypi/kraken

.. image:: https://img.shields.io/travis/MarcoNastasi/kraken.svg
        :target: https://travis-ci.com/MarcoNastasi/kraken

.. image:: https://readthedocs.org/projects/kraken/badge/?version=latest
        :target: https://kraken.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A multi-recipient and destination messaging server.


* Free software: MIT license
* Documentation: https://kraken.readthedocs.io.


Features
--------

The project is still in its early stages, at present all the project is capable off is sending an email after receiving a REST call

Configuration
-------------

tbd

Usage
-------
To run the program, run the following from inside the kraken subfolder
.. code-block:: python
    uvicorn kraken:app --reload

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
