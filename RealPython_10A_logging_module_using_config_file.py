#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 18 13:19:23 2021
@author: rohit
"""
import logging
import logging.config

logging.config.fileConfig(fname='RealPython_10A_logging_module_using_config_file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger.debug('This is a debug message')
