#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 20:18:27 2021
@author: rohit
"""
import logging
name = 'John'
logging.basicConfig(filename='RealPython_07_logging_module_log_dynamic_data_log.log', filemode='w')
logging.error('%s logged an error', name)
