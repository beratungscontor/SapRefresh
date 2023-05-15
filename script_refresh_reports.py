# -*- coding: utf-8 -*-
"""
Created on 3/29/2021
Author: Arnold Souza
Email: arnoldporto@gmail.com
"""
import os
from sapRefresh.sap_refresh import refresh_auto_reports
from sapRefresh.Core import Connection as Conn
from sapRefresh.Core.base_logger import get_logger

logger = get_logger(__name__, os.environ.get('LOG_PATH'))


try:
    refresh_auto_reports()
    logger.info("The Workbook refresh was done successfully!")
except Exception as e:
    # send error to the logger
    logger.critical(f"Couldn't refresh the data. ({' | '.join(str(item) for item in e.args)})")
    # send error by email
    msg_mail = f"Couldn't refresh the data. ({' | '.join(str(item) for item in e.args)})"
    #Conn.send_email(msg_mail, 'ERROR', 'SAP Refresh - Refresh Reports')