import time

from flask_restful import Resource

from common.base_parser import urlParse
from common.errors import ArgException
from common.util import getVideoByFormat, getNormalVideoByUrl, getTimeUrls


class Urls(Resource):
    def post(self):
        time1 = time.time()
        parse = urlParse.copy()
        args = parse.parse_args()
        url = args['url']
        if args['format'] is not None:
            ft = args['format']
            video_list = getVideoByFormat(url, ft)
        else:
            video_list = getNormalVideoByUrl(url)

        if len(video_list) == 0:
            raise ArgException

        if 'time' in args:
            if args['time']:
                urls_json = getTimeUrls(video_list)
                time2 = time.time()
                return {
                    'status': 200,
                    'result': 'success',
                    'content': urls_json,
                    'parse_time': time2 - time1}

        time2 = time.time()
        return {'status': 200,
                'result': 'success',
                'url': video_list,
                'parse_time': time2 - time1}
