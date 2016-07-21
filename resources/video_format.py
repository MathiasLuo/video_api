from flask import request
from flask_restful import Resource

from common.errors import ArgException
from common.util import getVideoFormats


class Format(Resource):
    def post(self):
        url = request.form['url']
        data = getVideoFormats(url)
        if len(data) == 0:
            raise ArgException
        return {'status': 200,
                'result': 'success',
                'format': data}
