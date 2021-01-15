#!/usr/bin/env python3
"""The HTTP API application.

The model class is used to configure the Flask application that implements the
required HTTP routes.
"""

from flask_psc_model import create_app
from model_lib.model import ModelName

app = create_app(ModelName)

if __name__ == '__main__':
    app.main()
