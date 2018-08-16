#!/usr/bin/env python3

import warnings
import sys 
import _creds
import require 
import functions.generic_functions as gen


account = raw_input('Enter the twitter handle you wish to analyze: @')
data = gen.user_deets(account)
data.user_details()
data.user_timeline()
