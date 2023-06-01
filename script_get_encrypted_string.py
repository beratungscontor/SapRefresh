# -*- coding: utf-8 -*-
"""
Created on 15/05/2023
Author: Felix von Streng
Email: felix.vonstreng@beratungscontor.com
"""

import os
import msvcrt
import sapRefresh.Core.Cripto as crypto
from sapRefresh.Core.base_logger import get_logger

logger = get_logger(__name__, os.environ.get('LOG_PATH'))

try:
    while True:
        print("Geben Sie den String ein der verschlüsselt werden soll und drücken sie ENTER (oder 'q' zum Beenden): ")
        
        user_input = input()

        if user_input.lower() == 'q':
            break
        
        secret_string = crypto.secret_encode(user_input)
        #user_input += key.decode("utf-8")
        
        print(f"The secret string {secret_string} is successful generated")
except Exception as e:
    # send error to the logger
    logger.critical(f"Couldn't generate secret string. ({' | '.join(str(item) for item in e.args)})")