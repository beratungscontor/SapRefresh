# -*- coding: utf-8 -*-
"""
Created on 15/05/2023
Author: Felix von Streng
Email: felix.vonstreng@beratungscontor.com
"""

import os
import sapRefresh.Core.Cripto as crypto
from sapRefresh.Core.base_logger import get_logger

logger = get_logger(__name__, os.environ.get('LOG_PATH'))

try:
    secret_string = crypto.secret_encode("my secret string")
    logger.info(f"The secret string {secret_string} is successful generated")
except Exception as e:
    # send error to the logger
    logger.critical(f"Couldn't generate secret string. ({' | '.join(str(item) for item in e.args)})")