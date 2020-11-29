#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Basics
# 
# This file holds all kinds of basic functionality needed
# in other classes. 
#
# ----------------------------------------------------------

# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------
import os
import constants
from datetime import datetime

# ----------------------------------------------------------
# GLOBAL VARIABLES
# ----------------------------------------------------------
LOGFILE_PATH = "icsscanner.log"


# ----------------------------------------------------------
# LOGGING
# ----------------------------------------------------------


def log(msg, log_level):
    """
    Used for logging purpose.
    Message won't be seen in terminal and
    will only be written to LOGFILE

    loglevel is an integer:
    0 -> [INFO]
    1 -> [WARNING]
    2 -> [ERROR]
    """
    # no logging if not wanted
    if not constants.DEBUG:
        return

    # choose mode -> if file doesn't exist, then create it
    mode = 'a' if os.path.exists(LOGFILE_PATH) else 'w'

    # get current time
    now = datetime.now()

    # format datetime string 
    formatted_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # Write, or better append, message to file
    with open(LOGFILE_PATH, mode) as f:
        f.write(str(get_log_level(log_level)) + "[" + formatted_time_string + "]: " + msg + "\n")


def get_log_level(log_level):
    """
    Returns Loglevel as string
    """
    return {
        0: "[INFO]",
        1: "[WARNING]",
        2: "[ERROR]"
    }[log_level]


