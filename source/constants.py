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
CONSOLE_PREFIX = "icscon > "

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
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    accessible integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL
                                )"""
