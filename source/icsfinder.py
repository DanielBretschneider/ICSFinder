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
    startupChecks()


def startupChecks():
    """
    Check if has active internet connection
    """
    # check internet connection 
    util.checkInternetConnectivity()


# ----------------------------------------------------------
# START OF PROGRAM
# ----------------------------------------------------------
if __name__ == "__main__":
    basics.log("Program started", 0)
    basics.displayMessage("ICSFINDER v1.0 started")
    main()
