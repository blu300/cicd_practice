from flask import Flask, request

test_app = Flask(__name__)

from src.app import routes
