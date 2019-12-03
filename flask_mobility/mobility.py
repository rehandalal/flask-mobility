import re

from flask import _request_ctx_stack as stack


class Mobility(object):
    def __init__(self, app=None):
        self.app = app

        if self.app is not None:
            self.init_app(self.app)

    def init_app(self, app):
        self.app = app
        app.config.setdefault("MOBILE_USER_AGENTS", "android|fennec|iemobile|iphone|opera (?:mini|mobi)|mobile")
        app.config.setdefault("MOBILE_COOKIE", "mobile")

        self.USER_AGENTS = re.compile(app.config.get("MOBILE_USER_AGENTS"))

        @app.before_request
        def before_request():
            ctx = stack.top
            if ctx is not None and hasattr(ctx, "request"):
                self.process_request(ctx.request)

    def process_request(self, request):
        ua = request.user_agent.string.lower()
        mc = request.cookies.get(self.app.config.get("MOBILE_COOKIE"))

        request.MOBILE = mc == "on" or (mc != "off" and self.USER_AGENTS.search(ua))
