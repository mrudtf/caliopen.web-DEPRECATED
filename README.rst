caliopen.web
============

CaliOpen Web Application is the HTTP entry point of CaliOpen infrastructure.

It requires some other CaliOpen modules.

Refer to [caliopen.github.io](http://caliopen.github.io/) for full installation
and development instructions.

Installation
------------

> Discalaimer: Those instructionsare for this module only. If you are looking
> for how to install a full CaliOpen service, you should go to
> [caliopen.github.io](http://caliopen.github.io/)

To install local dependencies, use [pip](https://pip.pypa.io/en/latest/):

:::
    pip install -e ".[dev,test]"

Note that caliopen.web depends on:

* [caliopen.core](https://github.com/caliopen/caliopen.core),
* [caliopen.api](https://github.com/caliopen/caliopen.api),
* [caliopen.config](https://github.com/caliopen/caliopen.config)

Tests
-----

Tests are launched using [nose](https://nose.readthedocs.org/en/latest/).

:::
    nosetests -sxv gandi/web/tests/*.py

