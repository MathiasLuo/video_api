import re
from flask import request
from flask.ext import restful

from common.util import getVideoFormats


class Format(restful.Resource):
    def post(self):
        try:
            url = request.form['url']
            data = getVideoFormats(url)
            return {'format': data,
                    'status': 'success'
                    }
        except TimeoutError:
            return {
                'error': 'time out',
                'status': 'fail'
            }
        except:
            return {'error': 'args error',
                    'status': 'fail'}
