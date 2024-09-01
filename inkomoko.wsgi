#!/usr/bin/python
import os
import sys
import site
import logging

# Add the app's directory to the PYTHONPATH
sys.path.insert(0, '/apps/python/inkomoko/')

# Add the site-packages of the chosen virtualenv to work with
sys.path.insert(0, '/apps/python/inkomoko/venv/lib/python3.9/site-packages')

from  main import app as application

