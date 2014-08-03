import unittest

from flask import Flask, render_template_string
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template, mobilized


class DecoratorsTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        Mobility(app)

        @app.route('/')
        @mobile_template('{mobile/}template.html')
        def index(template):
            return render_template_string(template)

        # Default View
        def mobilize():
            return render_template_string('False')

        # Mobilized view
        @app.route('/mobilize')
        @mobilized(mobilize)
        def mobilize():
            return render_template_string('True')

        self.app = app
        self.client = app.test_client()

    def test_mobile_template_user_agent(self):
        """Test the mobile_template decorator"""

        # Check without mobile User-Agent header
        assert b'template.html' == self.client.get('/').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', 'android')]
        response = self.client.get('/', headers=headers)
        assert b'mobile/template.html' == response.data

    def test_mobile_template_cookie(self):
        assert b'template.html' == self.client.get('/').data

        MOBILE_COOKIE = self.app.config.get('MOBILE_COOKIE')

        self.client.set_cookie('localhost', MOBILE_COOKIE, 'on')
        assert b'mobile/template.html' == self.client.get('/').data

        self.client.set_cookie('localhost', MOBILE_COOKIE, 'off')
        assert b'template.html' == self.client.get('/').data

    def test_mobilized_user_agent(self):
        """Test the mobilized decorator"""

        # Check without mobile User-Agent header
        assert b'False' == self.client.get('/mobilize').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', 'android')]
        assert b'True' == self.client.get('/mobilize', headers=headers).data

    def test_mobilized_cookie(self):
        assert b'False' == self.client.get('/mobilize').data

        MOBILE_COOKIE = self.app.config.get('MOBILE_COOKIE')

        self.client.set_cookie('localhost', MOBILE_COOKIE, 'on')
        assert b'True' == self.client.get('/mobilize').data

        self.client.set_cookie('localhost', MOBILE_COOKIE, 'off')
        assert b'False' == self.client.get('/mobilize').data
