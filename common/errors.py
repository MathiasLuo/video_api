class ArgException(Exception):
    pass


error = {
    'ArgException': {
        'msg': "args error",
        'status': 400,
        'info': 'fail'
    },
    'Exception': {
        'msg': "unknown error",
        'status': 404,
        'info': 'fail'
    },
    'TimeoutError': {
        'status': 504,
        'msg': 'time out',
        'info': 'fail'
    }
}
