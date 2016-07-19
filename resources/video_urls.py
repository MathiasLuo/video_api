import json
import re
import time

import sys
from flask import request
from flask.ext import restful

from common.util import getVideoByFormat, getNormalVideoByUrl
from common.util import getVideoJsonInfo


class Urls(restful.Resource):
    def post(self):
        try:
            time1 = time.time()
            url = request.form['url']
            if 'format' in request.form:
                ft = request.form['format']
                video_list = getVideoByFormat(url, ft)
            else:
                video_list = getNormalVideoByUrl(url)
            print(video_list)
            if 'time' in request.form:
                if request.form['time']:
                    urls_json = []
                    for index in range(len(video_list)):
                        u = video_list[index].strip()
                        video_json = json.loads(getVideoJsonInfo("%s" % u))
                        time_length = video_json['format']['duration']
                        file_size = video_json['format']['size']
                        urls_json.append({
                            "size": file_size,
                            "seconds": time_length,
                            "number": index,
                            "url": u
                        })
                    time2 = time.time()
                    return {'content': urls_json,
                            'status': 'success',
                            'parse_time': time2 - time1}
            time2 = time.time()
            return {'url': video_list,
                    'parse_time': time2 - time1,
                    'status': 'success'}
        except TimeoutError:
            return {
                'error': 'time out',
                'status': 'fail'
            }
        except:
            return {'error': 'args error',
                    'status': 'fail'}
