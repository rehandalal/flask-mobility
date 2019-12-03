import pytest

from flask import Flask, render_template_string
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template, mobilized


class TestDecorators(object):
    @pytest.fixture()
    def app(self):
        app = Flask(__name__)
        Mobility(app)

        @app.route("/")
        @mobile_template("{mobile/}template.html")
        def index(template):
            return render_template_string(template)

        # Default View
        def mobilize():
            return render_template_string("False")

        # Mobilized view
        @app.route("/mobilize")
        @mobilized(mobilize)
        def mobilize():
            return render_template_string("True")

        return app

    def test_mobile_template_user_agent(self, app):
        """Test the mobile_template decorator"""
        client = app.test_client()

        # Check without mobile User-Agent header
        assert b"template.html" == client.get("/").data

        # Check with mobile User-Agent header
        headers = [("User-Agent", "android")]
        response = client.get("/", headers=headers)
        assert b"mobile/template.html" == response.data

    def test_mobile_template_cookie(self, app):
        client = app.test_client()

        assert b"template.html" == client.get("/").data

        MOBILE_COOKIE = app.config.get("MOBILE_COOKIE")

        client.set_cookie("localhost", MOBILE_COOKIE, "on")
        assert b"mobile/template.html" == client.get("/").data

        client.set_cookie("localhost", MOBILE_COOKIE, "off")
        assert b"template.html" == client.get("/").data

    def test_mobilized_user_agent(self, app):
        """Test the mobilized decorator"""
        client = app.test_client()

        # Check without mobile User-Agent header
        assert b"False" == client.get("/mobilize").data

        # Check with mobile User-Agent header
        headers = [("User-Agent", "android")]
        assert b"True" == client.get("/mobilize", headers=headers).data

    def test_mobilized_cookie(self, app):
        client = app.test_client()

        assert b"False" == client.get("/mobilize").data

        MOBILE_COOKIE = app.config.get("MOBILE_COOKIE")

        client.set_cookie("localhost", MOBILE_COOKIE, "on")
        assert b"True" == client.get("/mobilize").data

        client.set_cookie("localhost", MOBILE_COOKIE, "off")
        assert b"False" == client.get("/mobilize").data
