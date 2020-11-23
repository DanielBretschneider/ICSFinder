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
        basics.display_warning("No database file found in 'db' folder")
        basics.log("database file was create: " + constants.DATABASE_PATH + constants.DATABASE_FILE, 0)

        # create connection
        try:
            # connection to db
            connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
            basics.display_warning("Database created at '" + constants.DATABASE_PATH + constants.DATABASE_FILE + "'")
            basics.log("Database created at '" + constants.DATABASE_PATH + constants.DATABASE_FILE + "'", 0)

            # create table 'devices'
            create_database_table(connection, constants.SQL_STATEMENT_INITIAL_DEVICES_TABLE)

            # return db connection
            return connection
        except Exception as e:
            basics.log("Error while connecting to database! \n" + str(e), 0)

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


def insert(ip, keywords, accessible, last_successful_ping, creation_date, http_access):
    """
    INSERT into 'devices' table in database
    """
    # create insert statement
    insert_statement = """INSERT INTO devices (ip_address, keywords, accessible, last_success_ping,creation_date,
                            http_accessible)
                          VALUES ('""" + ip + "', '" + keywords + "', " + accessible + ", '" + last_successful_ping +\
                            "', '" + creation_date + "', " + http_access + ")"

    try:
        # execute insert statement
        # connection to db
        connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute(insert_statement)
        connection.commit()
    except Exception as e:
        basics.log("Error while executing sql-statement \n" + insert_statement + "\nError:\n" + str(e), 0)


def print_found_devices():
    """
    Print already discovered devices as formatted table.
    """
    try:
        # database connection
        connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
        cursor = connection.execute("SELECT id, ip_address, keywords FROM devices")
        found_records = cursor.fetchall()

        # print table header
        print_devices_table_header()

        # print found resources
        for record in found_records:
            print_device_formatted(record)

    except Exception as e:
        basics.log("Error while trying to connect to database. \nError:\n" + str(e), 0)


def print_device_with_id(id):
    """
    Print device with given ID
    """
    try:
        # database connection
        connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
        cursor = connection.execute("SELECT id, ip_address, keywords FROM devices WHERE id=" + str(id))
        record = cursor.fetchone()
        print_devices_table_header()
        print_device_formatted(record)
    except Exception as e:
        basics.log("Error while trying to connect to database. \nError:\n" + str(e), 0)


def print_devices_with_keyword(keyword):
    """
    Print device with given ID
    """
    try:
        # database connection
        connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
        cursor = connection.execute("SELECT id, ip_address, keywords FROM devices WHERE keywords LIKE \'%" +
                                    str(keyword) + "%\'")
        records = cursor.fetchall()
        print_devices_table_header()

        # print found resources
        for record in records:
            print_device_formatted(record)
    except Exception as e:
        basics.log("Error while trying to connect to database. \nError:\n" + str(e), 0)


def print_device_formatted(record):
    """
    Print single Record Formatted
    """
    record_lst = list(record)
    print(str(record_lst[0]) + "\t" + str(record_lst[1]) + "\t" + str(record_lst[2]))


def print_devices_table_header():
    """
    Print formatted header for terminal table.
    """
    print('\033[1;34m' + "ID\tIP Address\tKeywords" + '\033[0m')


def count_found_devices():
    """
    Print total number of already discovered devices.
    """
    try:
        # database connection
        connection = sqlite3.connect(constants.DATABASE_PATH + constants.DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) from devices')
        cur_result = cursor.fetchone()
        print("Total: " + str(cur_result[0]))
    except Exception as e:
        basics.log("Error while trying to connect to database. \nError:\n" + str(e), 0)
