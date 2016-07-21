import flask_restful
from flask import Flask

from common.errors import error
from resources.hello_world import HelloWorld
from resources.url_by_dl import Url
from resources.video_format import Format
from resources.video_urls import Urls

app = Flask(__name__)
api = flask_restful.Api(app, errors=error)

api.add_resource(HelloWorld, "/")
api.add_resource(Format, "/format")
api.add_resource(Urls, "/urls")
api.add_resource(Url, '/other_url')

if __name__ == '__main__':
    app.run()
