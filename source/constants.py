#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Constants
# 
# This file just exists for holding constants need in other 
# classes. 
#
# ----------------------------------------------------------

#
# LOGFILE location
#
PATH_LOGFILE = "/home/db/dev/ICSFinder/log/icsfinderlog.log"

#
# CONSOLE PREFIX
#
CONSOLE_PREFIX = '\033[1;31m' + "icscon " + '\033[0m' + "> "

#
# DATBASE NAME
#
DATABASE_FILE = "icsfinder.db"

#
# PATH TO DB FOLDER
#
DATABASE_PATH = "/home/db/dev/ICSFinder/db/"

#
# SHODAN API KEY
#
SHODAN_API_KEY_FILE = "/home/db/dev/shodankey/key.txt"

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
