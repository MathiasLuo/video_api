import flask_restful
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from common import errors
from resources.hello_world import HelloWorld
from resources.url_by_dl import Url
from resources.video_format import Format
from resources.video_urls import Urls

app = Flask(__name__)
api = flask_restful.Api(app, errors=errors)

api.add_resource(HelloWorld, "/")
api.add_resource(Format, "/format")
api.add_resource(Urls, "/urls")
api.add_resource(Url, '/other_url')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(port=8080)
