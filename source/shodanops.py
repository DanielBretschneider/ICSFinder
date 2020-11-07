#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Shodan Operations
#
# Everything concering shodan
#
# ----------------------------------------------------------
# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------
import constants


# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------


def get_shodan_key():
    """
    Read contents of shodan api key file
    """
    api_key = ""

    with open(constants.SHODAN_API_KEY_FILE, "r") as api_key_file:
        api_key = api_key_file.read()

    return api_key

