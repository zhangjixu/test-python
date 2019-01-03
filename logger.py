# -*- coding: UTF-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_LEVEL = logging.INFO
LOG_PATH = '/Users/jixuzhang/Documents/workspaces/python/test-python/logs/log'

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT, datefmt=DATE_FORMAT)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
# stream_handler.setLevel(LOG_LEVEL)

file_handler = TimedRotatingFileHandler(LOG_PATH, 'D', 1, 0, encoding='utf-8')
# 设置后缀
file_handler.suffix = '%Y-%m-%d.log'
file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
file_handler.setLevel(LOG_LEVEL)

fh = TimedRotatingFileHandler('/Users/jixuzhang/Documents/workspaces/python/test-python/logs/time.log', 'D', 1, 0, encoding='utf-8')
fh.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
fh.setLevel(LOG_LEVEL)

log = logging.getLogger(name='root')
log.setLevel(LOG_LEVEL)
log.addHandler(file_handler)

logg = logging.getLogger(name='log')
logg.setLevel(LOG_LEVEL)
logg.addHandler(fh)