import functools
import re

from flask import g


def mobile_template(template):
    """
    Mark a function as mobile-ready and pass a mobile template if g.is_mobile.

    For example::

        @mobile_template('a/{mobile/}b.html')
        def view(template=None):
            ...


    if ``g.is_mobile=True`` the template will be `a/mobile/b.html`.
    if ``g.is_mobile=False`` the template will be `a/b.html`.

    This function is useful if the mobile view uses the same context but a
    different template.

    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            is_mobile = g.get("is_mobile", None)
            kwargs["template"] = re.sub(r"{(.+?)}", r"\1" if is_mobile else "", template)
            return f(*args, **kwargs)

        return wrapper

    return decorator


def mobilized(normal_fn):
    """
    Replace a view function with a normal and mobile view.

    For example::

        def view():
            ...

        @mobilized(view)
        def view():
            ...


    The second function is the mobile version of view. The original
    function is overwritten, and the decorator will choose the correct
    function based on ``g.is_mobile``.

    """

    def decorator(mobile_fn):
        @functools.wraps(mobile_fn)
        def wrapper(*args, **kwargs):
            if not g.is_mobile:
                return normal_fn(*args, **kwargs)
            return mobile_fn(*args, **kwargs)

        return wrapper

    return decorator
