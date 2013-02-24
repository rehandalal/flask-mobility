==============
Flask-Mobility
==============

A Flask extension to simplify building mobile-friendly sites.

.. image:: https://api.travis-ci.org/rehandalal/flask-mobility.png

What does this do?
==================

This extension detects whether a mobile site is requested and it
modifies the ``request`` object accordingly.

Decorators are provided to make mobilizing views easier.


Configuration
=============

There are two settings that you can change in the config for your
application:


**MOBILE_USER_AGENTS**
    A regex for detecting mobile user agents.

    Defaults to: ``'android|fennec|iemobile|iphone|opera (?:mini|mobi)'``


**MOBILE_COOKIE**
    The name of the cookie to set if the user prefers the mobile site.

    Defaults to: ``'mobile'``


Changes to the ``request`` Object
=================================

If the current request is for the mobile site, ``request.MOBILE =
True``. At all other times ``request.MOBILE = False``.


How is the value of ``request.MOBILE`` determined?
==================================================

``request.MOBILE`` will be set to ``True`` if one of the following
cases are satisfied:

1. The user agent string in the request headers matches
   ``MOBILE_USER_AGENTS`` and the ``MOBILE_COOKIE`` is not set to
   ``off``.
2. ``MOBILE_COOKIE`` is set to ``on``


Decorators
==========

mobile_template
---------------

This decorator is used to pass an alternate template name to a view
function for mobile requests::

    from flask.ext.mobility.decorators import mobile_template

    @mobile_template('dir/{mobile/}template.html')
    def view(template):
        ...


This will pass through ``'dir/mobile/template.html'`` as ``template``
where ``request.MOBILE`` is set to ``True``. When ``request.MOBILE``
is ``False`` it will pass through ``'dir/template.html'`` as
``template``.


mobilized
---------

This decorator is used to specify an alternate mobilized view function
for a view::

    from flask.ext.mobility.decorators import mobilized

    def view():
        ...

    @mobilized(view)
    def view():
        ...


In the example above the first ``view`` function is used for the
normal site and the second function is used to show the mobile site.
