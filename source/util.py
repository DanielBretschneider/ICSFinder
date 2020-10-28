#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------
# Utils
# 
# Holds essential functions only needed one time, or for 
# special purposes
#
# ----------------------------------------------------------
import requests
import basics

# ----------------------------------------------------------
# CHECK INTERNET CONNECTIVITY
# ----------------------------------------------------------
def checkInternetConnectivity():
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
        basics.displayMessage("Host has internet connection")
    except requests.ConnectionError:
        basics.log("Attempt to ping '" + url + "' failed. Either host has no connection or remote host is down.", 0)
        basics.displayMessage("Seems like host has no internet connection. See more information in /log/icsfinderlog.log!")
        basics.displayMessage("Exit.")    
        exit()
