import itertools
import hashlib
import time
import json
import os

# TODO: IMPROVE SPEED AND THREAD BRUTE FORCE METHOD!

path = os.path.dirname(__file__)
settings_file = 'settings.json'
with open(os.path.join(path, settings_file), 'r') as f:
    settings = json.load(f)


# Guesses from a list of common passwords
def guess_common_passwords(user_hash):
    print('Checking password hash against list of known passwords...')
    for guess in common_passwords.split('\n'):
        hashed_guess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        if hashed_guess == user_hash:
            print("The password has has been cracked and will be output to the password file!")
            password_file.write('Hash: ' + str(hashed_guess + ' Password: ') + str(guess) + '\n')
            password_file.close()
            quit()
        else:
            print("Password guess ", str(guess), " does not match, trying next...")


# Brute force guessing given a character set
def brute_force_password(user_hash, char_set):
    print('Starting Brute Force Method')
    print('Using character set: {} and range of {} to {}'.format(str(char_set), range_min, range_max))
    for item in range(range_min, range_max):
        for guess in itertools.product(char_set, repeat=item):
            guess = ''.join(guess)
            hashed_guess = hashlib.sha1(guess.encode('utf-8')).hexdigest()
            if hashed_guess == user_hash:
                print("The password has has been cracked and will be output to the password file!")
                password_file.write('Hash: ' + str(hashed_guess + ' Password: ') + str(guess) + '\n')
                password_file.close()
                quit()
    print('Brute force guess exhausted for character set and range. Exiting program.\n'
          'Try increasing range and character set.')
    quit()


# Loading config settings
char_set = settings['characterSet']
range_min = settings['minLength']
range_max = settings['maxLength']
user_hash = settings['hash']

# Open the common passwords database and assign it to the common_passwords variable
common_passwords_file = open('common_passwords.txt', 'r')
common_passwords = common_passwords_file.read()

# Opens the cracked passwords file as append mode. This allows for mass storage of cracked passwords.
password_file = open('cracked_passwords.txt', 'a')

if settings['database'] == 'true':
    guess_common_passwords(user_hash)
    print('No match has been found in the database...\nMoving on to different method...')
    time.sleep(1)
if settings['bruteForce'] == 'true':
    brute_force_password(user_hash, char_set)
