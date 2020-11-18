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
import os
import basics
import shodan


# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------


def get_shodan_key():
    """
    Read contents of shodan api key file
    """
    api_key = ""

    with open(constants.SHODAN_API_KEY_FILE, "r") as api_key_file:
        api_key = api_key_file.read().replace("\n", "")

    return api_key


def get_api_connection():
    # get key from key file
    api = shodan.Shodan(get_shodan_key())

    # return connection
    return api


def get_external_ip():
    """
    Print external ip of host
    """
    # output external ip
    exit_code = os.system('shodan myip')

    # if exit_code != then shodan isn't installed
    if exit_code != 0:
        basics.display_message("This command only works if shodan is installed on host!")


def get_shodan_info():
    """
    Returns information about the current API key, such as a list of add-ons and other
    features that are enabled for the current user’s API plan.
    """
    # output external ip
    exit_code = os.system('shodan info')

    # if exit_code != then shodan isn't installed
    if exit_code != 0:
        basics.display_message("This command only works if shodan is installed on host!")


def shodan_search(command):
    """
    Shodan search request
    Prints IP + data
    """
    try:
        # Search Shodan
        results = get_api_connection().search(command)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    except shodan.APIError as e:
        basics.display_warning("There was an error with your query.")
        basics.log(e.value, 2)


def shodan_host(command):
    """
    Get information on a specific IP
    """
    # extract ip
    ip_address = command.split(" ")[1]

    try:
        # Lookup the host
        host = get_api_connection().host(ip_address)

        # Print general info
        print("""
                IP: {}
                Organization: {}
                Operating System: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

        # Print all banners
        for item in host['data']:
            print("""
                        Port: {}
                        Banner: {}
    
                """.format(item['port'], item['data']))
    except shodan.APIError as e:
        basics.display_warning("No information available for that IP.")


def systemcmd(cmd):
    """
    Run system command
    """
    os.system(cmd)


def shodan_internal_search(command):
    """
    BA spezifisch: Wird über cmd Argumente angesteuert
    Speichert Daten in Datenbank
        - IP
        - keyword
        - ICMP Erreichbarkeit
    """
