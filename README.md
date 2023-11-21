# Flask Mobility

A Flask extension to simplify building mobile-friendly sites.

![PyPI](https://img.shields.io/pypi/v/flask-mobility.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-mobility.svg)

[![CircleCI](https://img.shields.io/circleci/project/github/rehandalal/flask-mobility.svg)](https://circleci.com/gh/rehandalal/flask-mobility)
[![Documentation](https://img.shields.io/readthedocs/flask-mobility/latest.svg)](http://flask-mobility.readthedocs.io/en/latest/?badge=latest)

This extension detects whether a mobile site is requested and it
modifies the Flask global `g` object accordingly.

Decorators are provided to make mobilizing views easier.

### Documentation

Full documentation is available at: 
http://flask-mobility.readthedocs.org/en/latest/


### Install

To install:
```
$ pip install Flask-Mobility
```

You can also install the [development version](https://github.com/rehandalal/flask-mobility/tarball/master#egg=Flask-Mobility-dev):
```
$ pip install Flask-Mobility==dev
```

or:
```
$ git clone git://github.com/rehandalal/flask-mobility.git
$ mkvirtualenv flaskmobility
$ python setup.py develop
$ pip install -r requirements.txt
```

### Test

To run tests from a tarball or git clone:
```
$ python setup.py test
```
