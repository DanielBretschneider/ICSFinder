#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Lite version of ICSFinder
#
# Only responsibility is to automatically collect ICS 
# information via shodan searches 
#
# ----------------------------------------------------------
# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------
import os
import requests
import basics
import shodan
import sqlite3
from datetime import datetime


# ----------------------------------------------------------
# GLOBAL FUNCTIONS
# ----------------------------------------------------------
# path to database
DATABASE_PATH = "/share/icsfinder_database.db"

# Create table statement
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

# list of keywords
KEYWORD_LIST_PATH = "/home/pi/ICSScanner/list/searches.txt"

# shodan API key
SHODAN_API_KEY_FILE = "/home/pi/ICSScanner/shodankey/key.txt"

# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------
def main():
    """
    Main Method
    """
    # get current time
    now = datetime.now()

    # format datetime string
    formatted_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # terminate log
    basics.log("Process started (" + formatted_time_string + ")", 0)
    
    # create connection to database
    create_database_connection()

    # get key
    shodankey = str(get_shodan_key())

    # open API connection
    api = shodan.Shodan(shodankey)

    # get keywords as list
    keywords = get_search_keywords()

    # start searching
    for keyword in keywords:
        basics.log("Processing keyword: '" + keyword + "'", 0)
        shodan_search(keyword, api)

    # terminate log
    basics.log("Process terminated (" + formatted_time_string + ")", 0)
    exit()


        
def get_shodan_key():
    """
    Read contents of shodan api key file
    """
    api_key = ""

    with open(SHODAN_API_KEY_FILE, "r") as api_key_file:
        api_key = api_key_file.read().replace("\n", "")

    return api_key


def get_search_keywords():
    """
    Reads contents of ~/ICSScanner/list/searches.txt
    for here are all keywords stored that should be
    searched for

    1 keyword per lime
    """
    with open(KEYWORD_LIST_PATH) as file_in:
        lines = []
        for line in file_in.readlines():
            lines.append(line.replace("\n", ""))
    
    basics.log("Found " + str(len(lines)) + " keywords inside '" + KEYWORD_LIST_PATH + "'", 0)
    
    return lines


def shodan_search(keyword, api):
    """
    Shodan search request
    Prints IP + additional data and inserts data into database.

    id INTEGER PRIMARY KEY,
    ip_address TEXT NOT NULL,
    keywords TEXT NOT NULL,
    accessible INTEGER NOT NULL,
    last_success_ping TEXT NOT NULL,
    creation_date TEXT NOT NULL,
    http_accessible INTEGER NOT NULL

    """
    # get current time
    now = datetime.now()

    # format datetime string
    formatted_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    try:
        results = api.search(keyword + ' country:AT')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            # IP Address
            ip = str(result['ip_str'])
            # Accessible over ICMP
            icmp_acc = str(check_icmp(result['ip_str']))
            # Accessible over HTTP
            http_acc = str(check_http(result['ip_str']))

            # insert into database
            insert(ip, keyword + ' country:AT', icmp_acc,
                str(formatted_time_string), str(formatted_time_string),
                http_acc)
            # log
            basics.log("Found IP :" + ip + "\tICMP: " + icmp_acc + "\tHTTP: " + http_acc, 0)
    except shodan.APIError as e:
        basics.log(e.value, 2)


def check_icmp(ip):
    """
    Test if given IP address can be pinged
    via ping -c 1
    """
    # try pinging ip
    response = os.system("ping -c 1 " + ip + " > /dev/null")

    # and then check the response...
    if response == 0:
        return True
    else:
        return False

    return pingstatus


def check_http(ip):
    """
    Check if given IP address is accessible via
    http.
    """
    try:
        # try reaching IP via http
        response = requests.Session()
        response_code = response.get("http://" + ip, timeout=(3, 5))

        # check response code
        if response_code.ok:
            return True
        else:
            return False
    except Exception:
        return False


def create_database_connection():
    """
    Creates SQLite3 database in case 
    the database doesn't already exist
    """
    connection = None

    # check if file exists
    if not check_if_file_exists(DATABASE_PATH):
        # create database file
        create_file(DATABASE_PATH)

        # log db file creation
        basics.log("database file was created: " + DATABASE_PATH, 0)

        # create connection
        try:
            # connection to db
            connection = sqlite3.connect(DATABASE_PATH)
            basics.log("Database created at '" + DATABASE_PATH + "'", 0)

            # create table 'devices'
            create_database_table(connection, SQL_STATEMENT_INITIAL_DEVICES_TABLE)

            # return db connection
            return connection
        except Exception as e:
            basics.log("Error while connecting to database! \n" + str(e), 0)

    else:
        # create connection
        try:
            # connect to db
            connection = sqlite3.connect(DATABASE_PATH)
            basics.log("Database connection established. path: '" + DATABASE_PATH + "'", 0)

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
        basics.log("Table 'devices' was created inside " + DATABASE_PATH, 0)
        basics.log("table devices has been created in database using following statement: \n", 0)
        basics.log(str(SQL_STATEMENT_INITIAL_DEVICES_TABLE), 0)
    except Exception as e:
        basics.log("Error while executing sql-statement \n" + create_table_sql_statement + "\nError:\n" + str(e), 0)


def check_if_file_exists(filename):
    """
    check if file exists
    """
    if os.path.exists(filename):
        return True
    # return False if not existing
    return False


def create_file(filename):
    """
    creates file with :param: filename
    """
    open(filename, "w").close()



def insert(ip, keywords, accessible, last_successful_ping, creation_date, http_access):
    """
    INSERT into 'devices' table in database
    """
    # create insert statement
    insert_statement = """INSERT INTO devices (ip_address, keywords, accessible, last_success_ping,creation_date,
                            http_accessible)
                          VALUES ('""" + ip + "', '" + keywords + "', " + accessible + ", '" + last_successful_ping +\
                            "', '" + creation_date + "', " + http_access + ")"

    # check if device already has been discovered
    if duplicate_check(ip):
        try:
            # execute insert statement
            # connection to db
            connection = sqlite3.connect(DATABASE_PATH)
            cursor = connection.cursor()
            cursor.execute(insert_statement)
            connection.commit()
        except Exception as e:
            basics.log("Error while executing sql-statement \n" + insert_statement + "\nError:\n" + str(e), 0)
    else:
        basics.log("Device with IP address " + ip + " has already been inserted into database, no action required", 0)


def duplicate_check(ip):
    """
    Check if g. IP address already exists in database
    True if it is a new device, False if it already has an entry
    """
    select_statement = "SELECT ip_address FROM devices WHERE ip_address='" + ip + "';"

    # if fetched records > 0 -> IP exists
    try:
        # database connection
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute(select_statement)
        data = cursor.fetchall()

        if len(data) == 0:
            return True

        return False
    except Exception as e:
        basics.log("Error while trying to connect to database. \nError:\n" + str(e), 0)


# ----------------------------------------------------------
# START OF PROGRAM
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
