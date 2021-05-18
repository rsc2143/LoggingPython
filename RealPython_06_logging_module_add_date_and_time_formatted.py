#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 19:57:23 2021
@author: rohit
"""
import logging
logging.basicConfig(filename='RealPython_06_logging_module_add_date_and_time_formatted.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged out')