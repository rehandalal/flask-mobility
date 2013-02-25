import re

from flask import _request_ctx_stack as stack


class Mobility(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app
        app.config.setdefault('MOBILE_USER_AGENTS',
            'android|fennec|iemobile|iphone|opera (?:mini|mobi)|mobile')
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
