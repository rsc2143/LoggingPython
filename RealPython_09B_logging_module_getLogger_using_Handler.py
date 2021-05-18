#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 20:58:42 2021
@author: rohit
"""
import logging

logger = logging.getLogger(__name__)

# Creating Handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('RealPython_09B_logging_module_getLogger_using_Handler_log.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

'''
Here, logger.warning() is creating a LogRecord that holds all the information of the event and passing it to all
 the Handlers that it has: c_handler and f_handler.

c_handler is a StreamHandler with level WARNING and takes the info from the LogRecord to generate an output in
 the format specified and prints it to the console. f_handler is a FileHandler with level ERROR, and it ignores 
 this LogRecord as its level is WARNING.

When logger.error() is called, c_handler behaves exactly as before, and f_handler gets a LogRecord at the level
 of ERROR, so it proceeds to generate an output just like c_handler, but instead of printing it to console,
  it writes it to the specified file in this format:

2018-08-03 16:12:21,723 - __main__ - ERROR - This is an error
'''