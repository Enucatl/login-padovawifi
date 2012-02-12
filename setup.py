#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function
import sys

print("Hi! Welcome to login-padovawifi.")
print("I'm going to check if you installed the mechanize module...")
try:
    import mechanize
    print("mechanize found (OK!)")
except ImportError:
    print("""could not find the mechanize module. Please install it.
If you are running an ubuntu system, just type:
            
            sudo apt-get install python-mechanize""")
    sys.exit(1)

print("""Beware! The password is going to be saved as plain text.
Encryption is not yet supported. Do you want to continue? """, end='')
cont = raw_input("[S/n] ")
if cont is "n":
    print("Exiting.")
    sys.exit(1)

username = raw_input("Enter your padovawifi username: ")
password = raw_input("Enter your padovawifi password: ")

file_name = "padovawifi_password"
with open(file_name, 'w') as output_file:
    output_file.write(username)
    output_file.write('\n')
    output_file.write(password)
    output_file.write('\n')
