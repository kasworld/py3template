#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2015 SeukWon Kang (kasworld@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""write program discription
made by kasw
copyright 2013
Version"""

Version = '1.0.0'

import os
import io
import sys
import os.path
import math
import random
import re
import datetime
import time
import string
import pprint
import uuid
import urllib
import re
import optparse
import struct
import multiprocessing
import binascii
import itertools
import functools
import logging
import signal


def sigstophandler(signum, frame):
    print('User Termination')
# signal.signal(signal.SIGINT, sigstophandler)


def getLogger(level=logging.DEBUG):
    # create logger
    logger = logging.getLogger('noname')
    logger.setLevel(level)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s:%(levelno)s:%(levelname)s: %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger


def logsample():
    log = getLogger()
    log.warning('warning')
    log.info('info')
    log.critical('critical')
    log.error('error')


def runtest():
    pass

if __name__ == "__main__":
    print(sys.version)
    print(__doc__, Version)

    # logsample()

    runtest()

    print(os.path.dirname(__file__))
    print(os.path.dirname(os.path.abspath(sys.argv[0])))
    print(__file__)
    print(sys.argv[0])

    # raw_input('Press Enter to End. >')


# vim:ts=4:sw=4:et
