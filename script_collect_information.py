# -*- coding: utf-8 -*-
"""
Created on 3/29/2021
Author: Arnold Souza
Email: arnoldporto@gmail.com
"""
import os
from sapRefresh.sap_refresh import collect_information
from sapRefresh.Core.base_logger import get_logger

logger = get_logger(__name__, os.environ.get('LOG_PATH'))

try:
    collect_information()
    logger.info("The information collection was done successfully!")
except Exception as e:
    # send error to the logger
    logger.critical(f"Couldn't refresh the data. ({' | '.join(str(item) for item in e.args)})")
