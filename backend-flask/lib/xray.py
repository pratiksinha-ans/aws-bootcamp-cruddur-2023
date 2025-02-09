# X-RAY ----------
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

import os
from flask import current_app as app

def init_xray(app):
   xray_url = os.getenv("AWS_XRAY_URL")
   xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
   XRayMiddleware(app, xray_recorder)