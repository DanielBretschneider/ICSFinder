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
import util


# ----------------------------------------------------------
# GLOBAL VARIABLES
# ----------------------------------------------------------


# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------
def main():
    """
    Main method
    """
    # starting checks 
    startupChecks()

    # start icsfinder console
    startICSFinderConsole()


def startupChecks():
    """
    Check if has active internet connection
    """
    # check internet connection 
    util.checkInternetConnectivity()

    # TODO add checks for shodan api key etc.
    basics.displayMessage("Start gathering ICS information")


def startICSFinderConsole():
    """
    Starts interactive console
    """
    while True:
        # read in user input
        icscommand = util.getICSConsoleCommand()
        basics.log("User command was '" + icscommand + "'", 0)

        # switch 
        if (icscommand == "exit"):
            basics.log("Exiting icsfinder", 0)
            basics.displayMessage("Exiting icsfinder")
            exit()
        elif (icscommand == "help"):
            util.printHelpMessage()
        elif (icscommand == ""):
            continue
        else:
            basics.displayMessage("'" + icscommand + "' is no valid command. Write 'help' for futher information.")
            basics.log("'" + icscommand + "' is no valid command. Write 'help' for futher information.", 0)
        

# ----------------------------------------------------------
# START OF PROGRAM
# ----------------------------------------------------------
if __name__ == "__main__":
    basics.log("Program started", 0)
    basics.displayMessage("ICSFINDER v1.0 started")
    main()
