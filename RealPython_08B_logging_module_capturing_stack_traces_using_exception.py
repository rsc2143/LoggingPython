#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 20:37:32 2021
@author: rohit
"""
import logging
a = 5
b = 0

logging.basicConfig(filename='RealPython_08B_logging_module_capturing_stack_traces_log.log', filemode='w')
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")