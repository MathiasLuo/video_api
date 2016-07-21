import json
import os

import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function.func_name, str(t1 - t0)))
        return result

    return function_timer


def getVideoJsonInfo(url):
    video_json = os.popen('ffprobe -v quiet -print_format json -show_format -show_streams "%s"' % url).read()
    return video_json


def getJsonByUrl(url):
    j = os.popen('youtube-dl -j "%s"' % url).read()
    str_list = j.split('\n')
    str_list.pop(len(str_list) - 1)
    content = {}
    for entry in str_list:
        for s in json.loads(entry)["formats"]:
            format_id = s["format_id"]
            if format_id in content:
                content[format_id].append(s["url"])
            else:
                content[format_id] = []
                content[format_id].append(s["url"])
    return content


def getNormalVideoByUrl(url):
    data = os.popen('you-get --url "%s"' % url).read()
    return getUrls(data)


def getVideoByFormat(url, ft):
    data = os.popen('you-get --format=%s --url "%s"' % (ft, url)).read()
    return getUrls(data)


def getVideoFormats(url):
    data = os.popen('you-get --info "%s"' % url).read()
    format_list = []
    for s in data.split('\n'):
        if s.find('format:') != -1:
            s = s.split(":")
            format_list.append(s[1].strip())
    return format_list


def getUrls(str_url):
    p = 'Real URLs:'
    ll = str_url.split(p)
    if len(ll) > 1:
        urls = ll[1].split('\n')
        urls.pop(len(urls) - 1)
        urls.pop(0)
        return urls
    else:
        for ss in str_url.split('\n'):
            if ss.find('http://') != -1:
                s = ss.replace("'", "").split(',')
                return s
        return []


def getTimeUrls(urls):
    urls_json = []
    for index in range(len(urls)):
        u = urls[index].strip()
        video_json = json.loads(getVideoJsonInfo("%s" % u))
        time_length = video_json['format']['duration']
        file_size = video_json['format']['size']
        urls_json.append({
            "size": file_size,
            "seconds": time_length,
            "number": index,
            "url": u
        })
        return urls_json
