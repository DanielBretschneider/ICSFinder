#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Main File
# 
# Program starts from here on 
#
# ----------------------------------------------------------
__author__  = "Daniel Bretschneider"
__file__    = "icsfinder.py"
__version__ = "1.0"
__created__ = "28.10.2020"

# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------
import basics
import constants
import database
import util


# ----------------------------------------------------------
# GLOBAL VARIABLES
# ----------------------------------------------------------
DB_CONNECTION = None


# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------


def main():
    """
    Main method
    """
    # starting checks 
    startup_checks()

    # start icsfinder console
    start_interactive_console()


def startup_checks():
    """
    Check if has active internet connection
    """
    # check internet connection 
    util.check_internet_connectivity()

    # create database if not already existing
    database_connection = database.create_database_connection()

    # create tables if necessary
    database.create_database_table(database_connection, constants.SQL_STATEMENT_INITIAL_DEVICES_TABLE)

    # TODO add checks for shodan api key etc.
    basics.display_message("Start gathering ICS information")


def start_interactive_console():
    """
    Starts interactive console
    """
    while True:
        # read in user input
        command = util.get_next_ics_command()
        basics.log("User command was '" + command + "'", 0)

        # switch 
        if command == "exit":
            basics.log("Exiting icsfinder", 0)
            basics.display_message("Exiting icsfinder")
            exit()
        elif command == "help":
            util.print_help_message()
        elif command == "":
            continue
        else:
            basics.display_message("'" + command + "' is no valid command. Write 'help' for futher information.")
            basics.log("'" + command + "' is no valid command. Write 'help' for futher information.", 0)
        

# ----------------------------------------------------------
# START OF PROGRAM
# ----------------------------------------------------------
if __name__ == "__main__":
    basics.log("Program started", 0)
    basics.display_message("ICSFINDER v1.0 started")
    main()
