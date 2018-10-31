# -*- coding: UTF-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_LEVEL = logging.INFO
LOG_PATH = 'log_time.log'

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT, datefmt=DATE_FORMAT)

fh = logging.TimedRotatingFileHandler(LOG_PATH, 'D', 1, 0, encoding='utf-8')
fh.setFormatter(logging.Formatter(LOG_FORMAT))
fh.setLevel(LOG_LEVEL)

