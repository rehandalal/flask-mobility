import pytest

from flask import Flask, render_template_string, request
from flask_mobility import Mobility


class MobilityTestCase(object):
    @pytest.fixture()
    def app(self):
        app = Flask(__name__)
        Mobility(app)

        @app.route("/")
        def index():
            assert isinstance(request.MOBILE, bool)
            tpl = "{% if request.MOBILE %}True{% else %}False{% endif %}"
            return render_template_string(tpl)

        return app

    def test_detect_mobile_user_agent(self, app):
        """Check that mobile user agents are properly detected"""
        client = app.test_client()

        # Check without mobile User-Agent header
        assert b"False" == client.get("/").data

        # Check with mobile User-Agent header
        headers = [("User-Agent", "android")]
        assert b"True" == client.get("/", headers=headers).data

    def test_mobile_cookie(self, app):
        client = app.test_client()

        """Check that the mobile cookie value is respected"""
        MOBILE_COOKIE = app.config.get("MOBILE_COOKIE")

        # Check cookie is set to 'on'
        client.set_cookie(MOBILE_COOKIE, value="on")
        assert b"True" == client.get("/").data

        # Check cookie is set to 'off'
        client.set_cookie(MOBILE_COOKIE, value="off")
        headers = [("User-Agent", "android")]
        assert b"False" == client.get("/", headers=headers).data
