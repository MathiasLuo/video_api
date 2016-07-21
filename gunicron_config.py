
bind = '127.0.0.1:5000'  # 绑定的端口
workers = 1  # worker数量
backlog = 2048
timeout = 30


def worker_abort(worker):
    raise TimeoutError
