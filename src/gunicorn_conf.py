# gunicorn_conf.py
from multiprocessing import cpu_count
from typing import Final


bind: Final[str] = "127.0.0.1:7905"

# Worker Options
workers: Final[int] = cpu_count() + 1
worker_class: Final[str] = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel: Final[str] = 'error'
accesslog: Final[str] = 'logs/access_log'
errorlog: Final[str] =  'logs/error_log'