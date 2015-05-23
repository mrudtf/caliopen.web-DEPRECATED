caliopen.web
============

.. image:: https://travis-ci.org/CaliOpen/caliopen.web.svg?branch=features%2Fuser-account
    :target: https://travis-ci.org/CaliOpen/caliopen.web

CaliOpen Web Application is the HTTP entry point of CaliOpen infrastructure.

It requires some other CaliOpen modules.

Refer to `caliopen.github.io <http://caliopen.github.io/>`_ for full installation
and development instructions.

Installation
------------

::

    Disclaimer: Those instructions are for this module only. If you are looking
    for how to install a full CaliOpen service, you should go to
    `caliopen.github.io <http://caliopen.github.io/>`_

To install local dependencies, use `pip <https://pip.pypa.io/en/latest/>`_:

::

    pip install -e ".[dev,test]"

Note that caliopen.web depends on:

* `caliopen.config <https://github.com/caliopen/caliopen.config>`_
* `caliopen.storage <https://github.com/caliopen/caliopen.storage>`_,
* `caliopen.core <https://github.com/caliopen/caliopen.core>`_,
* `caliopen.messaging <https://github.com/caliopen/caliopen.messaging>`_,
* `caliopen.api <https://github.com/caliopen/caliopen.api>`_,

Tests
-----

Tests are launched using `nose <https://nose.readthedocs.org/en/latest/>`_.

::

    nosetests -sxv caliopen/web/tests/*.py

