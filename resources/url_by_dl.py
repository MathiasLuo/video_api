import json
import time
from flask import request
from flask.ext import restful

from common.util import getJsonByUrl, getVideoJsonInfo


class Url(restful.Resource):
    def get(self):
        pass

    def post(self):
        try:
            time1 = time.time()
            url = request.form['url']
            j = getJsonByUrl(url)
            if 'time' in request.form:
                if request.form['time']:
                    content = []
                    for key in j.keys():
                        # key
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
                    return {'content': content,
                            'parse_time': time2 - time1}
            # print(j[key])
            # print("dict[%s]=%d" % key, len(j[key]))

            time2 = time.time()
            return {
                'url': j,
                'parse_time': time2 - time1
            }
        except TimeoutError:
            return {
                'error': 'time out',
                'code': 504
            }
        except:
            return {'error': 'args error',
                    'code': 404}
