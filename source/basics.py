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
    # choose mode -> if file doesn't exist, then create it
    mode = 'a' if os.path.exists(constants.PATH_LOGFILE) else 'w'

    # get current time
    now = datetime.now()

    # format datetime string 
    formatted_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # Write, or better append, message to file
    with open(constants.PATH_LOGFILE, mode) as f:
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


# ----------------------------------------------------------
# PRINT TO SCREEN
# ----------------------------------------------------------
def display_message(msg):
    """
    Display message about status, progress or 
    just an information on screen. Will be logged.
    """
    print("[*] " + msg)
    log("[basics.displayMessage()] -> (\"" + msg + "\")", 0)


def display_warning(msg):
    """
    Display message about status, progress or 
    just an information on screen. Will be logged.
    """
    print('\33[93m' + "[*] " + msg + '\033[0m')
    log("[basics.displayWarning()] -> (\"" + msg + "\")", 0)
