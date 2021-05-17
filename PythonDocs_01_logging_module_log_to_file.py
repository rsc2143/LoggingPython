#/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Monday May 17 18:08:24 2021
@author: rohit
"""
import logging
logging.basicConfig(filename='example.log',  level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

