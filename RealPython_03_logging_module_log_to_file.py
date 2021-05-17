#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 18:03:29 2021
@author: rohit
"""
import logging
import os
print(str(os.getcwd()))
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
#This is an error