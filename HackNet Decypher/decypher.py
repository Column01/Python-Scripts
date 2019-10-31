# Author: Colin Andress
# Filename : decypher.py
# Date: 28/04/2019
# Description: Hacknet file decrypter


def encrypt(data, code):
    ret = []
    for i in range(len(data)):
        # Convert the string into the corresponding number
        val = ord(data[i])
        # Attempt to encrypt it using the algorithm found in game
        newval = (val * 1822) + MaxValue / 2 + code
        # Append the encrypted value to a temp array
        ret.append(int(newval))
    return ret


def decrypt(data, code):
    ret = []
    for j in range(len(data)):
        # Decrypt the input using a reversed formula from the encryption
        newval = ((MaxValue / 2 + code) - int(data[j])) / -1822
        # Convert the output number to a character
        newvalstring = chr(int(newval))
        # Append it to the list
        ret.append(newvalstring)
    return ret


def find_password(data):
    print("Trying to find a valid password for provided file... ")
    ret = []
    # Generate a blank reference header using no password
    base_header = encrypt("ENCODED", 0)
    # Get the encrypted header
    encrypted_header = data[2].split()
    for l in range(len(encrypted_header)):
        # Cast the chunk of the header to an integer
        encrypted_header[l] = int(encrypted_header[l])
        # Find the password offset for each item in the header and append it to our array
        password_test = int(encrypted_header[l]) - int(str(base_header[l]))
        ret.append(str(password_test))
    for k in range(len(ret)):
        # if the iteration of the password array is equal to the first item in the array, pass
        if ret[0] == ret[k]:
            pass
        # if it doesn't match, quit because we could not find a password
        else:
            print("Passwords do not match!")
            quit()
    # Get an encoded header example using the new password
    encoded_header = encrypt("ENCODED", int(ret[0]))
    for j in range(len(encoded_header)):
        # Check if it's a valid password and if it is, return the password
        if encoded_header[j] == encrypted_header[j]:
            print("Found valid password! Attempting to decrypt file...")
            return int(ret[0])
        # No valid password, quit program.
        else:
            print("Password not valid... Quiting program. Output: \n" + str(encoded_header) + "\n" + str(encrypted_header))
            quit()


def ask():
    ask1 = input("Would you like to encode or decode a file (Choices are e or d): ").lower()
    if ask1 != "e" and ask1 != "d":
        print(f'Invalid option "{ask1}". Please run program again!')
        raise SystemExit
    ask2 = input('What is the name of the file you wish to encrypt/decrypt? ')
    return ask1, ask2


def get_file(f):
    try:
        with open(f, "r") as r:
            ofile = r.read()
            return ofile
    except FileNotFoundError:
        return False


MaxValue = 65534
password = 5886
userInput = ask()
action = userInput[0]
infile = userInput[1]
file = get_file(infile)
# File doesn't exist
if file is False:
    print(f"File '{infile}' was not found. Did you forget to not include the file extension?"
          f"\nRun script again and try again.")
    raise SystemExit
# The user wants to encrypt. Build an encrypted file.
if action == "e":
    header = "#DEC_ENC::"
    encoded = str(encrypt("ENCODED", password)).replace(", ", " ").strip("[").strip("]") + "::"
    source = str(encrypt("Column01's Encoder. Find it on Github here: http://bit.ly/HackDecypher", password)).replace(", ", " ").strip("[").strip("]") + "::"
    infile_header = str(encrypt(infile, password)).replace(", ", " ").strip("[").strip("]") + "::"
    extension = str(encrypt(".txt", password)).replace(", ", " ").strip("[").strip("]") + "\n"
    encoded_message = encrypt(file, password)
    output = open("encoded_output.txt", "w+")
    output.write(header + infile_header + source + encoded + extension)
    print("Writing file header and metadata...")
    output.write("".join(str(encoded_message).replace(", ", " ").strip("[").strip("]")))
    print("Writing file contents to output in encoded form...")
# the user wants to decrypt so decrypt the file they provided
elif action == "d":
    filelist = file.strip("#DEC_ENC").replace('\n', "::").split("::")
    for item in filelist:
        try:
            filelist.remove('')
        except ValueError:
            pass
    solved_password = find_password(filelist)
    file_note = decrypt(filelist[0].split(), password)
    file_source = decrypt(filelist[1].split(), password)
    file_contents = decrypt(filelist[4].split(), solved_password)
    output = open("output.txt", "w+")
    output.write("".join(file_note) + "\n" + "".join(file_source) + "\n" + "".join(file_contents))
    print("Output written to file: output.txt")
