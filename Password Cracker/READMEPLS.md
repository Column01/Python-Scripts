# SHA1 Password-Cracker

## Disclaimer
This program is intended for learning purposes only. Any illegal usage of this program is the responsibility of its user. The creator is not legally responsible in any way for damage caused by this program. Users found using this program for illegal means will be reported to the authorities.

This program does not collect user data. 

If you find someone re-distributing this program, please report it on the issues section of the repository.

## Info
If your password is not in the common passwords database (I sure hope it isn't!) and you have the option set to true in the config, it will start a brute force hashing of your password with a character set defined in the settings file. This process is resource intensive and can take a long time, and might not even result with your password.

To maximize chances of success, make sure that your password has characters defined in the character set, and that the `range_max` variable is set to the maximum character count of your password.

If you do not want to use a certain cracking method, you can set it to `false` in the settings file.

Using **Ctrl+C** will exit out of the program.

## How to use it on Linux
1. Run this command to download the repository `git clone https://github.com/Column01/Password-Hasher` and extract it (alternatively, click [this link](https://github.com/Column01/Password-Hasher/archive/master.zip) to download it)
2. Open `password-hasher.py` in your favourite text editor or IDE
3. Replace `password` variable with your password (all character types are supported) and save it
4. Run `password-hasher.py` via terminal by following the instructions below
5. It will print the password hash to the console. Copy it and add it to the settings.json file
6. Run `password-cracker.py` via terminal by following the instructions below
7. Watch as it decrypts your password!

## How to use it on Windows
1. Download the repository [here](https://github.com/Column01/Password-Hasher/archive/master.zip) and extract it
2. Open `password-hasher.py` in your favourite text editor or IDE
3. Replace `password` variable with your password (all character types are supported) and save it
4. Run `password-hasher.py` via console by following the instructions below
5. It will print the password hash to the console. Copy it and add it to the settings.json file
6. Run `password-cracker.py` via console by following the instructions below
7. Watch as it decrypts your password!

## How to run python scripts

### Linux
```
cd /path/to/download
chmod +x password-cracker.py or chmod +x password-hasher.py
python password-cracker.py or python password-hasher.py
```

**Note:** To run python commands from terminal, you must add Python to your Path variable. It should be there by default, but if it throws an unknown command error (and you already have python installed), run the following command:

`export PATH="$PATH:/usr/local/bin/python"`

### Windows
```
cd /path/to/download
python password-cracker.py or python password-hasher.py
```

**Note:** To run python commands from CMD, you must add Python to your Path variable (provided it is already installed).

Follow [this guide](https://geek-university.com/python/add-python-to-the-windows-path/) to add it.

## Credits
A special thanks to NullByte Kody for the common password database as well as the base code for the algorithm to check it. You can find the blog post on it [here](https://null-byte.wonderhowto.com/how-to/use-beginner-python-build-brute-force-tool-for-sha-1-hashes-0185455/) and the NullByte YouTube channel [here](https://www.youtube.com/channel/UCgTNupxATBfWmfehv21ym-g). If you like this tool, then you certainly will like their YouTube channel!
