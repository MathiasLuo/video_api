import json
import time
from flask_restful import Resource

from common.base_parser import urlParse
from common.errors import ArgException
from common.util import getJsonByUrl, getVideoJsonInfo


class Url(Resource):
    def post(self):
        time1 = time.time()
        parse = urlParse.copy()
        args = parse.parse_args()
        url = args['url']
        j = getJsonByUrl(url)
        if len(j) == 0:
            raise ArgException
        if 'time' in args:
            if args['time']:
                content = []
                for key in j.keys():
                    urls_json = []
                    for index in range(len(j[key])):
                        u = j[key][index]
                        video_json = json.loads(getVideoJsonInfo("%s" % u))
                        time_length = video_json['format']['duration']
                        file_size = video_json['format']['size']
                        urls_json.append({
                            "size": file_size,
                            "seconds": time_length,
                            "number": index,
                            "url": u
                        })
                    content.append({
                        'format': key,
                        'url': urls_json
                    })
                time2 = time.time()
                return {
                    'status': 200,
                    'result': 'success',
                    'content': content,
                    'parse_time': time2 - time1}
        time2 = time.time()
        return {
            'status': 200,
            'result': 'success',
            'url': j,
            'parse_time': time2 - time1}
