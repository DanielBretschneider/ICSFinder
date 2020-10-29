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


# ----------------------------------------------------------
# CHECK INTERNET CONNECTIVITY
# ----------------------------------------------------------
def checkInternetConnectivity():
    """
    Check if user has internet connection
    """
    # url that will be accessed
    url = 'http://www.google.com/'

    # define timeout
    timeout = 5
     
    # logging info
    basics.displayMessage("Checking if host is connected to the internet")
    basics.log("Attemting to ping '" + url + "'", 0)

    # now try to access url
    try:
        _ = requests.get(url, timeout=timeout)
        basics.log("Successfully pinged '" + url + "'", 0)
        basics.displayMessage("Host is online")
    except requests.ConnectionError:
        basics.log("Attempt to ping '" + url + "' failed. Either host has no connection or remote host is down.", 2)
        basics.displayMessage("Seems like host has no internet connection. See more information in /log/icsfinderlog.log!")
        basics.displayMessage("Exit.")    
        exit()


# ----------------------------------------------------------
# GET ICSCONSOLE COMMAND
# ----------------------------------------------------------
def getICSConsoleCommand():
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
def printHelpMessage():
    """
    Prints help message 
    """
    # print Message
    print("\nICSFinder Command Overview" + "\n")
    printHelpCommand("help", "Show help message")
    printHelpCommand("show ip", "Show your external IP address")
    printHelpCommand("exit", "Exit ICSFinder\n")

    # log acitity
    basics.log("Printed help message", 0)


def printHelpCommand(command, description):
    """
    Print coloured and formatted command and description
    """
    print('\33[33m' + command + '\033[0m' + "\t - " + description)