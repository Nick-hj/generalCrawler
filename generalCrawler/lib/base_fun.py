# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 23:17
# @Author  : Haijun

import os
from loguru import logger as base_logger


def init_logger():
    '''
    日志
    '''
    base_path = os.path.join(os.getcwd(), 'logs')
    base_logger.add(os.path.join(base_path, 'spider_info_{time:YYYY-MM-DD}.log'),
                    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file.path} | {module} | {function} | {line} | {message}",
                    level="INFO", rotation="00:00", retention='6 days', enqueue=True, encoding='utf-8')
    base_logger.add(os.path.join('/data/logs', 'spider_error_{time:YYYY-MM-DD}.log'),
                    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file.path} | {module} | {function} | {line} | {message}",
                    level="ERROR", rotation="00:00", retention='6 days', enqueue=True, encoding='utf-8')
    return base_logger


logger = init_logger()
