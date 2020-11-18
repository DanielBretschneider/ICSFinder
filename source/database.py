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
import util

# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------


def create_database_connection():
    """
    Creates SQLite3 database in case 
    the database doesn't already exist
    """
    connection = None

    # check if file exists
    if not util.check_if_file_exists(constants.DATABASE_PATH + constants.DATABASE_FILE):
        # create database file
        util.create_file(constants.DATABASE_PATH + constants.DATABASE_FILE)

        # log db file creation
        basics.display_warning("No database file found in 'db' folder, so file was created at:  " +
                               constants.DATABASE_PATH + constants.DATABASE_FILE)
        basics.log("database file was create: " + constants.DATABASE_PATH + constants.DATABASE_FILE, 0)

        # create connection
        try:
            # connection to db
            connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
            basics.display_warning("Database created at '" + constants.DATABASE_PATH + constants.DATABASE_FILE + "'")
            basics.log("Database created at '" + constants.DATABASE_PATH + constants.DATABASE_FILE + "'", 0)

            # return db connection
            return connection
        except Exception as e:
            basics.log("Error while connecting to database! \n" + str(e), 0)

        create_database_table(connection, constants.SQL_STATEMENT_INITIAL_DEVICES_TABLE)

    else:
        # create connection
        try:
            # connect to db
            connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
            basics.display_message("Connection to database established")
            basics.log("Database connection established. path: '" + constants.DATABASE_PATH + constants.DATABASE_FILE + "'", 0)

            return connection
        except Exception as e:
            basics.log("Error while connecting to database! \n" + str(e), 0)

    # return connection anyways
    return connection


def create_database_table(db_connection, create_table_sql_statement):
    """
    create a table from the create_table_sql statement
    :param db_connection: Connection object
    :param create_table_sql_statement: a CREATE TABLE statement
    :return:
    """
    try:
        # execute table creation statement
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql_statement)
        db_connection.commit()

        # log table creation
        basics.display_warning("Table 'devices' was created inside " + constants.DATABASE_PATH +
                               constants.DATABASE_FILE)
        basics.log("table devices has been created in database using following statement: \n", 0)
        basics.log(str(constants.SQL_STATEMENT_INITIAL_DEVICES_TABLE), 0)
    except Exception as e:
        basics.log("Error while executing sql-statement \n" + create_table_sql_statement + "\nError:\n" + str(e), 0)


