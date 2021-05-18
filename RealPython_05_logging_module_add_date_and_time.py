#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 19:57:23 2021
@author: rohit
"""
import logging
logging.basicConfig(filename='RealPython_05_logging_module_add_date_and_time_log_file.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')