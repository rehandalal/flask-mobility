#!/usr/bin/env python
from flask import Flask, render_template
from flask.ext.mobility import Mobility, mobile_template

app = Flask(__name__)
Mobility(app)

@app.route('/')
@mobile_template('{mobile/}index.html')
def index(template):
    return render_template(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
