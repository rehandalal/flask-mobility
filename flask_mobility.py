import functools
import re
from flask import _request_ctx_stack as stack

class Mobility(object):

    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(app)
        else:
            self.app = None


    def init_app(self, app):
        app.config.setdefault('MOBILE_USER_AGENTS',
            'android|fennec|iemobile|iphone|opera (?:mini|mobi)')
        app.config.setdefault('MOBILE_COOKIE', 'mobile')

        self.USER_AGENTS = re.compile(app.config.get('MOBILE_USER_AGENTS'))

        @app.before_request
        def before_request():
            ctx = stack.top
            if ctx is not None and hasattr(ctx, 'request'):
                self.process_request(ctx.request)


    def process_request(self, request):
        ua = request.user_agent.string.lower()
        mc = request.cookies.get(self.app.config.get('MOBILE_COOKIE'))

        if (self.USER_AGENTS.search(ua) and mc != 'off') or mc == 'on':
            request.MOBILE = True
        else:
            request.MOBILE = False


# Decorators

def mobile_template(template):
    """
    Mark a function as mobile-ready and pass a mobile template if MOBILE.

    @mobile_template('a/{mobile/}b.html')
    def view(template=None):
    ...

    if request.MOBILE=True the template will be 'a/mobile/b.html'.
    if request.MOBILE=False the template will be 'a/b.html'.

    This function is useful if the mobile view uses the same context but a
    different template.
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            ctx = stack.top
            if ctx is not None and hasattr(ctx, 'request'):
                request = ctx.request
                fmt = {'mobile/': 'mobile/' if request.MOBILE else ''}
                kwargs['template'] = template.format(**fmt)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def mobilized(normal_fn):
    """
    Replace a view function with a normal and mobile view.

    def view(request):
    ...

    @mobilized(view)
    def view(request):
    ...

    The second function is the mobile version of view. The original
    function is overwritten, and the decorator will choose the correct
    function based on request.MOBILE.
    """
    def decorator(mobile_fn):
        @functools.wraps(mobile_fn)
        def wrapper(*args, **kwargs):
            ctx = stack.top
            if ctx is not None and hasattr(ctx, 'request'):
                request = ctx.request
                if not request.MOBILE:
                    return normal_fn(*args, **kwargs)
            return mobile_fn(*args, **kwargs)
        return wrapper
    return decorator
