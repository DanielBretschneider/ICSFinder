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
import database
import os
import util
import basics
import shodan
from datetime import datetime

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
    api = shodan.Shodan(str(get_shodan_key()))

    # return connection
    return api


def get_external_ip():
    """
    Print external ip of host
    """
    # output external ip
    exit_code = systemcmd('shodan myip')

    # if exit_code != then shodan isn't installed
    if exit_code != 0:
        basics.display_message("This command only works if shodan is installed on host!")


def get_shodan_info():
    """
    Returns information about the current API key, such as a list of add-ons and other
    features that are enabled for the current user’s API plan.
    """
    # output external ip
    exit_code = systemcmd('shodan info')

    # if exit_code != then shodan isn't installed
    if exit_code != 0:
        basics.display_message("This command only works if shodan is installed on host!")


def shodan_search(command):
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
    command = command[7:]

    # get current time
    now = datetime.now()

    # format datetime string
    formatted_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    try:
        # Search Shodan
        api = shodan.Shodan(str(get_shodan_key()))
        results = api.search(command + ' country:AT')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            # IP Address
            ip = str(result['ip_str'])
            # Accessible over ICMP
            icmp_acc = str(util.check_icmp(result['ip_str']))
            # Accessible over HTTP
            http_acc = str(util.check_http(result['ip_str']))

            # print information
            print('IP: ' + ip + "\tICMP: " + icmp_acc + "\tHTTP: " + http_acc)

            # insert into database
            database.insert(ip, command + ' country:AT', icmp_acc,
                            str(formatted_time_string), str(formatted_time_string),
                            http_acc)
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
Port: {}
Organization: {}
Operating System: {}
        """.format(host['ip_str'], get_host_port(host), host.get('org', 'n/a'), host.get('os', 'n/a')))

        # print additional data
        for item in host['data']:
            print(item['data'])

        # print connection info
        print("\nConnectivity")
        print("ICMP: " + str(util.check_icmp(ip_address)))
        print("HTTP: " + str(util.check_http(ip_address)))
    except shodan.APIError as e:
        basics.display_warning("No information available for that IP.")


def get_host_port(host):
    """
    Extract ports from shodan data for host information
    """
    # Print all banners
    for item in host['data']:
        if item['port'] != "":
            return item['port']

    # dummy return if no port declared
    return 'n/a'


def systemcmd(cmd):
    """
    Run system command
    """
    return os.system(cmd)


def locate_ip(command):
    """
    Returns geolocation of ip address
    """
    print("")
    systemcmd("curl https://api.hackertarget.com/geoip/?q=" + command.split(" ")[1])
    print("\n")
