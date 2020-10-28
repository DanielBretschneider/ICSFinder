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
def log(msg, loglevel):
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
    formattedTimeString = now.strftime("%d/%m/%Y %H:%M:%S")

    # Write, or better append, message to file
    with open(constants.PATH_LOGFILE, mode) as f:
        f.write(str(getLogLevel(loglevel)) + "[" + formattedTimeString + "]: " + msg + "\n")


def getLogLevel(loglevel):
    """
    Returns Loglevel as string
    """
    return {
        0 : "[INFO]",
        1 : "[WARNING]",
        2 : "[ERROR]"
    }[loglevel]

# ----------------------------------------------------------
# PRINT TO SCREEN
# ----------------------------------------------------------
def displayMessage(msg):
    """
    Display message about status, progress or 
    just an information on screen. Will be logged.
    """
    print("[*] " + msg)
    log("[displaymessage] -> (" + msg + ")", 0)