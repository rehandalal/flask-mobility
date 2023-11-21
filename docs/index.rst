================
 Flask-Mobility
================

.. contents::
   :local:


.. include:: ../README.rst


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


Changes to the global ``g`` Object
==================================

If the current request is for the mobile site, ``g.is_mobile ==
True``. At all other times ``g.is_mobile == False``.


How is the value of ``g.is_mobile`` determined?
===============================================

``g.is_mobile`` will be set to ``True`` if one of the following
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

    from flask_mobility.decorators import mobile_template

    @mobile_template('dir/{mobile/}template.html')
    def view(template):
        ...


This will pass through ``'dir/mobile/template.html'`` as ``template``
where ``g.is_mobile`` is set to ``True``. When ``g.is_mobile``
is ``False`` it will pass through ``'dir/template.html'`` as
``template``.


mobilized
---------

This decorator is used to specify an alternate mobilized view function
for a view::

    from flask_mobility.decorators import mobilized

    def view():
        ...

    @mobilized(view)
    def view():
        ...


In the example above the first ``view`` function is used for the
normal site and the second function is used to show the mobile site.


Example
=======

**example.py**

.. literalinclude:: example/example.py
   :language: python
   :linenos:


**templates/base.html**

.. literalinclude:: example/templates/base.html
   :language: html
   :linenos:


**templates/index.html**

.. literalinclude:: example/templates/index.html
   :language: html
   :linenos:


**templates/mobile/index.html**

.. literalinclude:: example/templates/mobile/index.html
   :language: html
   :linenos:


.. include:: ../CONTRIBUTORS
