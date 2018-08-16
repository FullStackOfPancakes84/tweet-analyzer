#!/usr/bin/env python3
import os 
from os import system
import functions.generic_functions as gen

try:
    from twython import Twython
    from termcolor import colored
except ImportError as e:
    os.system('pip install -r requirements.txt')
    from twython import Twython 
    from termcolor import colored 
    gen.clear()