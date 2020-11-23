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
import readline
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
    try:
        command = input(constants.CONSOLE_PREFIX)
    except KeyboardInterrupt as kie:
        basics.log("shutdown", 0)
        print("")
        exit()

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
    print_help_subtitle("General Commands")
    print_help_command("help\t", "Show help message")
    print_help_command("clear\t", "Clear Screen")
    print_help_command("exit\t", "Exit ICSFinder")
    print_help_subtitle("\nShow Commands")
    print_help_command("show apikey", "Show Shodan API key")
    print_help_command("show myip", "Show your external IP address")
    print_help_command("show info", "Returns information about current user’s API plan")
    print_help_command("show devices", "Print all already discovered devices")
    print_help_command("show device id", "Print database record of single device with 'id'")
    print_help_subtitle("\nExplore Shodan API")
    print_help_command("search\t", "Search commands works exactly as in Shodan CLI")
    print_help_command("host\t", "Get Information about an specific host")
    print_help_subtitle("\nDatabase Related Commands")
    print_help_command("db count", "Get current number of devices found")
    print_help_subtitle("\nOther useful commands")
    print_help_command("locate ip", "Returns geolocation of given IP address")

    # newline after help message
    print("")

    # log activity
    basics.log("Printed help message", 0)


def print_help_command(command, description):
    """
    Print coloured and formatted command and description
    """
    print('\33[33m' + command + '\033[0m' + "\t" + description)


def print_help_subtitle(command):
    """
    Print coloured and formatted command and description
    """
    print('\033[1;34m' + command + '\033[0m')


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


# ----------------------------------------------------------
# ICMP and HTTP connectivity checks
# ----------------------------------------------------------
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
        response_code = requests.head("http://" + ip)

        # check response code
        if response_code.ok:
            return True
        else:
            return False
    except requests.ConnectionError:
        print("failed to connect")

