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

        self.app = app.test_client()

    def test_mobile_template(self):
        """Test the mobile_template decorator"""

        # Check without mobile User-Agent header
        assert 'template.html' == self.app.get('/').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', 'android')]
        assert 'mobile/template.html' == self.app.get('/', headers=headers).data

    def test_mobilized(self):
        """Test the mobilized decorator"""

        # Check without mobile User-Agent header
        assert 'False' in self.app.get('/mobilize').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', 'android')]
        assert 'True' in self.app.get('/mobilize', headers=headers).data
