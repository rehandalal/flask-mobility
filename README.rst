Summary
=======

A Flask extension to simplify building mobile-friendly sites.

This extension detects whether a mobile site is requested and it
modifies the ``request`` object accordingly.

Decorators are provided to make mobilizing views easier.

`|travisimage|`_


Documentation
=============

Documentation is at
`<http://flask-mobility.readthedocs.org/en/latest/>`_.


Install
=======

To install::

    $ pip install Flask-Mobility


You can also install the development version
`<https://github.com/rehandalal/flask-mobility/tarball/master#egg=Flask-Mobility-dev>`_::

    $ pip install Flask-Mobility==dev


or::

    $ git clone git://github.com/rehandalal/flask-mobility.git
    $ mkvirtualenv flaskmobility
    $ python setup.py develop
    $ pip install -r requirements.txt


Test
====

To run tests from a tarball or git clone::

    $ python setup.py test

.. _|travisimage|: https://travis-ci.org/rehandalal/flask-mobility/
.. |travisimage| image:: https://api.travis-ci.org/rehandalal/flask-mobility.png
