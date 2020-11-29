#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Constants
# 
# This file just exists for holding constants need in other 
# classes. 
#
# ----------------------------------------------------------

from os.path import expanduser

#
# DEBUG
#
DEBUG = True

#
# ROOT FOLDER
#
ROOT = expanduser("~")

#
# ICSFINDER ROOT
#
PATH_ICSFINDER_ROOT = ROOT + "/ICSFinder"

#
# LOG FOLDER
#
PATH_LOG_FOLDER = PATH_ICSFINDER_ROOT + "/log"

#
# LOGFILE location
#
PATH_LOGFILE = PATH_LOG_FOLDER + "/icsfinderlog.log"

#
# SHODAN KEY FILE
#
PATH_SHODANKEY = PATH_ICSFINDER_ROOT + "/shodankey"

#
# CONSOLE PREFIX
#
CONSOLE_PREFIX = '\033[1;31m' + "icscon " + '\033[0m' + "> "

#
# PATH TO DB FOLDER
#
DATABASE_PATH = PATH_ICSFINDER_ROOT + "/db"

#
# DATBASE NAME
#
DATABASE_FILE = "/icsfinder.db"

#
# SHODAN API KEY
#
SHODAN_API_KEY_FILE = PATH_SHODANKEY + "/key.txt"

#
# Create table statement
#
SQL_STATEMENT_INITIAL_DEVICES_TABLE = """
                                CREATE TABLE IF NOT EXISTS devices (
                                    id INTEGER PRIMARY KEY,
                                    ip_address TEXT NOT NULL,
                                    keywords TEXT NOT NULL,
                                    accessible INTEGER NOT NULL,
                                    last_success_ping TEXT NOT NULL,
                                    creation_date TEXT NOT NULL,
                                    http_accessible INTEGER NOT NULL
                                )"""
