#!/usr/bin/env python3
import os 
from os import system, name 
import sys 
import _creds
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def user_details(account):
    clear()
    package = _creds.twitter.show_user(screen_name=account)
    criteria = ['name',
                'suspended', 
                'verified', 
                'location',
                'friends_count',
                'followers_count',
                'favourites_count',
                'statuses_count',
                'created_at',
                'time_zone',
                'geo_enabled',
                'lang'
                ]

    for key, value in package.iteritems():
        if key in criteria:
            
            icon = colored('[ + ] ', 'green', 'on_grey')
            key = colored('%s ' % (key), 'white', 'on_grey').encode('utf-8')
            value = colored('|| %s ' % (value), 'red', 'on_grey', attrs=['bold', 'blink']).encode('utf-8')
            print (icon + key + value)
        else:
            pass