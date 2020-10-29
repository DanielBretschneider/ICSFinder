#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Database
# 
# This file is responsible for all database activites.
#
# ----------------------------------------------------------

# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------
import sqlite3
import constants
import basics
import sys


# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------

def createDatabaseConnection():
    """
    Creates SQLite3 database in case 
    the database doesn't already exist
    """
    # connection to db database
    db_connection = None

    # if true tables have to be created
    databaseIsExisting = True

    if (basics.checkIfFileExists(constants.DATABASE_FILE)):
        basics.log("Database file already exists. Try connecting", 0)
        basics.displayMessage("Datbase file already exists. Try connecting.")
    else:
        basics.log("Database file not found. Will be created at '" + constants.DATABASE_FILE + "'", 0)
        basics.displayWarning("Database file not found. Will be created at '" + constants.DATABASE_FILE + "'")
        databaseIsExisting = False

    # try connecting
    try:
        # log activity
        basics.log("Attempting to create or open database file at: " + constants.DATABASE_FILE, 0)

        # open database connection
        db_connection = sqlite3.connect(constants.DATABASE_FILE)

        # if no error occured then connection will now be returned
        basics.log("Successfully connected to datbase; returning", 0)
        basics.displayMessage("Successfully connected to database.")
        
        # create table if file was created now
        if (databaseIsExisting == False):
            createTables(db_connection)

        # return connection
        return db_connection
    except:
        # log error connecting to db
        basics.log("Couldn't establish connection to database file at: +" + constants.DATABASE_FILE, 2)

        # dispaly error message
        basics.displayWarning("Couldn't establish connection to database file at: " + constants.DATABASE_FILE)


def createTables(db_connection):
    """
    This function will only be exexuted if 
    database file was initially created
    """
    # sql create table statement
    sql_create_devices_table = """CREATE TABLE IF NOT EXISTS ICSDevices (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    status_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""
    
    # if db_connection is not null
    try:
        # attempt to create tables
        basics.log("Attempting to create tables in database", 0)
        basics.displayMessage("Attempting to create tables in database as file was initially created")
        cursor = db_connection.cursor()
        cursor.execute(sql_create_devices_table)
        cursor.commit()
        cursor.close()
    except:
        # tables have been successfully created
        basics.log("Successfully created table ICSDevices inside database", 0)
        basics.displayMessage("Successfully created table ICSDevices inside database")
        pass


def printTableContents(db_connection):
    with db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM ICSDevices")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

