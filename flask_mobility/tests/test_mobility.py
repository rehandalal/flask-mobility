import unittest

from flask import Flask, render_template_string
from flask.ext.mobility import Mobility


class MobilityTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        Mobility(app)

        @app.route('/')
        def index():
            tpl = '{% if request.MOBILE %}True{% else %}False{% endif %}'
            return render_template_string(tpl)

        self.app = app.test_client()
        self.config = app.config

    def test_detect_mobile_user_agent(self):
        """Check that mobile user agents are properly detected"""

        # Check without mobile User-Agent header
        assert b'False' == self.app.get('/').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', 'android')]
        assert b'True' == self.app.get('/', headers=headers).data

    def test_mobile_cookie(self):
        """Check that the mobile cookie value is respected"""
        MOBILE_COOKIE = self.config.get('MOBILE_COOKIE')

        # Check cookie is set to 'on'
        self.app.set_cookie('localhost', MOBILE_COOKIE, 'on')
        assert b'True' == self.app.get('/').data

        # Check cookie is set to 'off'
        self.app.set_cookie('localhost', MOBILE_COOKIE, 'off')
        headers = [('User-Agent', 'android')]
        assert b'False' == self.app.get('/', headers=headers).data
