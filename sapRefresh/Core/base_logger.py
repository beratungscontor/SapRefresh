# -*- coding: utf-8 -*-
"""
Created on 3/14/2021
Author: Arnold Souza
Email: arnoldporto@gmail.com
"""
import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


def get_logger(logger_name, log_path):
    # string formatter
    format_string = '%(asctime)s | %(name)s | %(module)s | %(funcName)s | [%(levelname)s] | %(message)s'
    logFormatter = logging.Formatter(format_string, datefmt='%Y%m%d %H:%M')

    # initiate root logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # set up console logger
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logFormatter)
    logger.addHandler(console_handler)

    # set up file logger
    log_filename = datetime.now().strftime("%Y%m%d")
    location = log_path + f'\\{log_filename}.log'  # create a path do the log
    logfile_handler = TimedRotatingFileHandler(location, when='D', interval=1, backupCount=30)
    logfile_handler.setLevel(logging.INFO)  # do not print DEBUG messages to file
    logfile_handler.setFormatter(logFormatter)
    logger.addHandler(logfile_handler)

    os.environ['LOG_FILEPATH'] = location
    return logger

# Log some messages
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")
