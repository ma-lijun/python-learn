# gunicorn.conf
import logging
from logging.handlers import TimedRotatingFileHandler
import os, sys
import multiprocessing

from gunicorn.glogging import Logger

filepath = "./log/"
# when S M H D W 分别表示以秒、分钟、小时、天、周为日期分割时间周期
th_acc = TimedRotatingFileHandler(when="D", backupCount=7, filename=filepath + "access.log")
th_err = TimedRotatingFileHandler(when="D", backupCount=7, filename=filepath + "error.log")
th_acc.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s | %(message)s"))
th_err.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s | %(message)s"))

# gunicorn源码中不支持按日切分日志
class SplitLogger(Logger):
    def __init__(self, cfg):
        super(SplitLogger, self).__init__(cfg)
        self.access_log.addHandler(th_acc)
        self.error_log.addHandler(th_err)

# Server Socket
bind = ["0.0.0.0:5000"]
# 监听队列
backlog = 1024
chdir = "./"
timeout = 180

# Worker Processes
worker_class = "gevent"
workers = multiprocessing.cpu_count() * 2 + 1

# Logging
loglevel = "info"

access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = "./gunicorn_access.log"

error_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
errorlog = "./gunicorn_error.log"

logger_class = SplitLogger
