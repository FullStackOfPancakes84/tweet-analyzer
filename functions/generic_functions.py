#!/usr/bin/env python3
import os
from os import system, name 
import _creds
import require

''' define our function to clear the terminal screen '''
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux
    else:
        _ = system('clear')


''' Our user deets object expects an account to query '''
class user_deets(object):

    # Pass a screen name to the class
    def __init__(self, account):
        self.account = account 

    # Fetch specific details about this user 
    def user_details(self):
        clear()
        package = _creds.twitter.show_user(screen_name=self.account)
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
                
                icon = require.colored('[ + ] ', 'green', 'on_grey')
                key = require.colored('%s ' % (key), 'white', 'on_grey').encode('utf-8')
                value = require.colored('|| %s ' % (value), 'red', 'on_grey', attrs=['bold', 'blink']).encode('utf-8')
                print (icon + key + value)
            else:
                pass

    # Retrieve the most recent 200 tweets from this user 
    def user_timeline(self):
        count = 0
        ch = ''
        timeline = _creds.twitter.get_user_timeline(screen_name=self.account, include_rts=True, count=200)

        for tweet in timeline:
            count += 1
            ch = ch + ' '

        records = require.colored('[ %d ] ' % (count), 'yellow', 'on_grey')
        body = require.colored('tweets analyzed', 'white', 'on_grey')
        print (records + body)
        print (require.colored('%s' % (ch), 'white', 'on_green'))