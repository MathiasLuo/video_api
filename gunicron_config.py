import os
bind='127.0.0.1:5000' #绑定的端口
workers=1 #worker数量
backlog=2048
debug=True
timeout = 30
accesslog='/var/log/gunicorn/access.log'
errorlog='/var/log/gunicorn/error.log'
proc_name='gunicorn.pid'
pidfile='/var/log/gunicorn/debug.log'


def worker_abort(worker):
    raise TimeoutError