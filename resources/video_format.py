from flask_restful import Resource

from common.base_parser import baseParser
from common.errors import ArgException
from common.util import getVideoFormats


class Format(Resource):
    def post(self):
        parser = baseParser.copy()
        args = parser.parse_args()
        url = args['url']
        data = getVideoFormats(url)
        if len(data) == 0:
            raise ArgException
        return {'status': 200,
                'result': 'success',
                'format': data}
