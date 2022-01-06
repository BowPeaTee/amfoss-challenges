#! python3
# mail.py - Mails an account the given string from the given account in the command line.
# mail email string --syntax

import sys
from selenium import webdriver

email = sys.argv[1]
string = sys.argv[2]

browser = webdriver.Firefox()
browser.get('https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&su=&body=')

