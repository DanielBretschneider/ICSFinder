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
import shodanops


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
            exit()
        elif command == "help":
            util.print_help_message()
        elif command.startswith("show"):
            show_cmd(command)
        elif command.startswith("search"):
            shodan_search_command(command)
        elif command.startswith("host"):
            shodan_host_command(command)
        elif command.startswith("db"):
            database_operations(command)
        elif command == "clear":
            shodanops.systemcmd("clear")
        elif command == "":
            continue
        else:
            basics.display_warning("'" + command + "' is no valid command. Write 'help' for further information.")
            basics.log("'" + command + "' is no valid command. Write 'help' for further information.", 0)


# ----------------------------------------------------------
# ICS COMMAND HANDLING
# ----------------------------------------------------------
def get_splitted_command(command):
    # split cmd
    splitted_command = command.split(" ")

    # check if command has more arguments
    if len(splitted_command) == 1:
        basics.display_message("'" + command + "' is no valid command. Write 'help' for further information.")
        start_interactive_console()
    else:
        return splitted_command


def show_cmd(command):
    """
    'show' commands will be handled here
    """
    # split command
    split_command = get_splitted_command(command)

    if split_command[1] == "apikey":
        print(shodanops.get_shodan_key())
    elif split_command[1] == "myip":
        shodanops.get_external_ip()
    elif split_command[1] == "info":
        shodanops.get_shodan_info()
    elif split_command[1] == "devices":
        database.print_found_devices()
    else:
        basics.display_warning("'" + command + "' is no valid command. Write 'help' for further information.")


def shodan_search_command(command):
    """
    'search' commands will be handled here
    """
    shodanops.shodan_search(command)


def shodan_host_command(command):
    """
    'host' commands will be handled here
    """
    shodanops.shodan_host(command)


def database_operations(command):
    """
    Database commands will be handled here
    """
    # split command
    split_command = get_splitted_command(command)

    if split_command[1] == "count":
        database.count_found_devices()


# ----------------------------------------------------------
# START OF PROGRAM
# ----------------------------------------------------------
if __name__ == "__main__":
    basics.log("Program started", 0)
    basics.display_message("ICSFINDER v1.0 started")
    main()
