# Chatlog filter
# Copyright (C) 2019 Colin Andress
import os
import re

path = os.path.dirname(__file__)
# User input
inputFile = input('What is the name of the input file?\nFormat: filename.txt\nEnter Filename: ')
usernames = input('What are the names you would like to look for?\nFormat: Bob,Sally,George\nEnter Names: ').split(',')
outputFile = input('What would you like the output file to be named?\nFormat: filename.txt\nEnter Filename: ')

# Opens the chatlogs file
try:
    with open(inputFile, 'r') as f:
        chatlogs = f.readlines()
except FileNotFoundError:
    print('Chatlogs file not found. Please create a file called "chatlogs.txt" and place the chatlogs inside it')
for line in chatlogs:
    # Finds all matches for the list of names provided by the user
    if re.findall(r"(?=(" + '|'.join(usernames) + r"))", line):
        # Opens the output file, and creates it if it doesn't exist
        d = open(outputFile, 'w+')
        # Pulls the timestamp from the list item
        timestamp = line.split(']', 1)[0] + '] '
        # Pulls everything following the timestamp and removes the "BOT" prefix of all names
        message = line.split('] ', 1)[1][3:]
        # Writes the matches to the output file
        d.write(timestamp + message)
