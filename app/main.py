from flask import Flask
import logging

from flask_cors import CORS

logging.basicConfig(level=logging.DEBUG)


app = Flask(title="FindBus")
logging.info("Starting FindBus API")

origins = ["*"]
CORS(app, resources={r"/*": {"origins": origins}})
