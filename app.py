# !usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from pyvue_templates import render_template_index

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_index()

if __name__ == '__main__':
    app.run(debug=True)
