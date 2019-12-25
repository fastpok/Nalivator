# coding: utf-8

from flask import Flask
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/sse-stream')

@app.route('/')
def index():
  return 'hello'

@app.route('/hello')
def publish_hello():
  sse.publish({"message": "Hello!"}, type='greeting')
  return "Message sent!"
