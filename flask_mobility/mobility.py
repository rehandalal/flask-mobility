import re

from flask import g, request


class Mobility(object):
    def __init__(self, app=None):
        self.app = app

        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MOBILE_USER_AGENTS", "android|fennec|iemobile|iphone|opera (?:mini|mobi)|mobile")
        app.config.setdefault("MOBILE_COOKIE", "mobile")

        self.USER_AGENTS = re.compile(app.config.get("MOBILE_USER_AGENTS"))

        @app.before_request
        def before_request():
            ua = request.user_agent.string.lower()
            mc = request.cookies.get(app.config.get("MOBILE_COOKIE"))
            g.is_mobile = mc == "on" or (mc != "off" and self.USER_AGENTS.search(ua) is not None)
