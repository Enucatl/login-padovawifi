#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
import re
import mechanize
import sys

login_site = "http://login.padovawifi.it/"

print("opening browser")
br = mechanize.Browser()
text = br.open(login_site)
text = text.read()
logged_in = "Collegato a Padova WiFi" in text
if not logged_in:
    br.select_form(name="form1")
    print("username and password...")
    with open("padovawifi_password") as password_file:
        lines = password_file.readlines()
        br["UserName"] = lines[0].strip()
        br["Password"] = lines[1].strip()
        print("submitting...")
        br.submit()
    print("done.")
    sys.exit(0)
else:
    print("already logged in")
    sys.exit(0)
