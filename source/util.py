#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Utils
# 
# Holds essential functions only needed one time, or for 
# special purposes
#
# ----------------------------------------------------------

# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------
import requests
import basics
import constants
import os


# ----------------------------------------------------------
# CHECK INTERNET CONNECTIVITY
# ----------------------------------------------------------
def check_internet_connectivity():
    """
    Check if user has internet connection
    """
    # url that will be accessed
    url = 'http://www.google.com/'

    # define timeout
    timeout = 5
     
    # logging info
    basics.display_message("Checking if host is connected to the internet")
    basics.log("Attemting to ping '" + url + "'", 0)

    # now try to access url
    try:
        _ = requests.get(url, timeout=timeout)
        basics.log("Successfully pinged '" + url + "'", 0)
        basics.display_message("Host is online")
    except requests.ConnectionError:
        basics.log("Attempt to ping '" + url + "' failed. Either host has no connection or remote host is down.", 2)
        basics.display_message("Seems like host has no internet connection. See more information in /log/icsfinderlog.log!")
        basics.display_message("Exit.")
        exit()


# ----------------------------------------------------------
# GET ICSCONSOLE COMMAND
# ----------------------------------------------------------
def get_next_ics_command():
    """
    command line interface for icsfinder
    """
    # read user input
    command = input(constants.CONSOLE_PREFIX)

    # return given command without leading and trailing whitespace
    # and in lower case - for easier command proccessing
    return command.strip().lower()


# ----------------------------------------------------------
# PRINT HELP MESSAGE
# ----------------------------------------------------------
def print_help_message():
    """
    Prints help message 
    """
    # print Message
    print("\nICSFinder Command Overview" + "\n")
    print_help_command("help", "Show help message")
    print_help_command("show ip", "Show your external IP address")
    print_help_command("exit", "Exit ICSFinder\n")

    # log acitity
    basics.log("Printed help message", 0)


def print_help_command(command, description):
    """
    Print coloured and formatted command and description
    """
    print('\33[33m' + command + '\033[0m' + "\t - " + description)


# ----------------------------------------------------------
# I/O Operations
# ----------------------------------------------------------
def create_file(filename):
    """
    creates file with :param: filename
    """
    open(constants.DATABASE_PATH + constants.DATABASE_FILE, "w").close()


def check_if_file_exists(filename):
    """
    check if file exists
    """
    if os.path.exists(filename):
        return True
    # return False if not existing
    return False


def delete_file(filename):
    """
    deletes a file
    """
    os.remove(filename)
