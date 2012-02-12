#!/usr/bin/env python
#coding=utf-8

from __future__ import division, print_function
import sys
import os
import mechanize

login_site = "http://login.padovawifi.it/"
my_folder = sys.path[0]
password_filename = "padovawifi_password"
password_filename = os.path.join(my_folder, password_filename)

if not os.path.exists(password_filename):
    print("Password file 'padovawifi_password' not found!")
    sys.exit(1)

def logged_in(browser):
    """this function checks if you are logged in."""
    text = br.open(login_site)
    text = text.read()
    logged_in = "Collegato a Padova WiFi" in text
    return logged_in

print("opening browser")
br = mechanize.Browser()
if not logged_in(br):
    br.select_form(name="form1")
    print("reading username and password...")
    with open(password_filename) as password_file:
        lines = password_file.readlines()
        br["UserName"] = lines[0].strip()
        br["Password"] = lines[1].strip()
        print("submitting...")
        br.submit()
    if logged_in(br):
        print("Done.")
        sys.exit(0)
    else:
        print("Incorrect username or password.")
        sys.exit(1)
else:
    print("already logged in.")
    sys.exit(0)
