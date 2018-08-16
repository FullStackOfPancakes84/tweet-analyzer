#!/usr/bin/env python3
try:
    from twython import Twython
except ImportError as e:
    os.system('pip install -r requirements.txt')

APP_KEY = 'Your app key here'
APP_SECRET = 'Your app secret here'
OAUTH_TOKEN = 'Your oauth token here'
OAUTH_TOKEN_SECRET = 'Your oauth token secret here'


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)