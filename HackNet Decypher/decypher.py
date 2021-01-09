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
        newval = (val * 1822) + MAX_VALUE / 2 + code
        # Append the encrypted value to a temp array
        ret.append(int(newval))
    return ret


def decrypt(data, code):
    ret = []
    for j in range(len(data)):
        # Decrypt the input using a reversed formula from the encryption
        newval = ((MAX_VALUE / 2 + code) - int(data[j])) / -1822
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
    for i in range(len(encrypted_header)):
        # Cast the chunk of the header to an integer
        encrypted_header[i] = int(encrypted_header[i])
        # Find the password offset for each item in the header and append it to our array
        password_test = int(encrypted_header[i]) - int(str(base_header[i]))
        ret.append(str(password_test))
    for j in range(len(ret)):
        # if the iteration of the password array is equal to the first item in the array, pass
        if ret[0] == ret[j]:
            pass
        # if it doesn't match, quit because we could not find a password
        else:
            print("Passwords do not match!")
            quit()
    # Get an encoded header example using the new password
    encoded_header = encrypt("ENCODED", int(ret[0]))
    for k in range(len(encoded_header)):
        # Check if it's a valid password and if it is, return the password
        if encoded_header[k] == encrypted_header[k]:
            print("Found valid password! Attempting to decrypt file...")
            return int(ret[0])
        # No valid password, quit program.
        else:
            print("Password not valid... Quiting program. Output: \n" + str(encoded_header) + "\n" + str(encrypted_header))
            quit()


def ask():
    while True:
        ask1 = input("Would you like to encode or decode a file (Choices are e or d): ").lower()
        if ask1 not in ["e", "d"]:
            print(f'Invalid option "{ask1}".')
        else:
            break

    while True:
        ask2 = input('What is the name of the file you wish to encrypt/decrypt? ')
        if ask2 is None or isinstance(ask2, int):
            print("Please enter a valid input file name!")
        else:
            break
    return ask1, ask2


def get_file(f):
    try:
        with open(f, "r") as r:
            o_file = r.read()
            return o_file
    except FileNotFoundError:
        return False


# Some Constants
MAX_VALUE = 65534
# The default "empty" password was reverse engineered using C# and a dump of the game's code.
# the game uses "GetHashCode()" on an empty string and then it's casted to a unsigned short, which equals 5886
PASSWORD = 5886

# The header of all encoded files
HEADER = "#DEC_ENC::"
# The word "ENCODED" is used to determine if the password is correct in the game. Coincidentally, it can be used to find the password used to encrypt a file!
ENCODED = str(encrypt("ENCODED", PASSWORD)).replace(", ", " ").strip("[").strip("]") + "::"
# The source of the file is also included in the header of the files.
SOURCE = str(encrypt("Column01's Encoder. Find it on Github here: http://bit.ly/HackDecypher", PASSWORD)).replace(", ", " ").strip("[").strip("]") + "::"

# Get some input from the user and parse it
user_input = ask()
action = user_input[0]
in_file = user_input[1]
input_file = get_file(in_file)
# File doesn't exist
if input_file is False:
    print(f"File '{in_file}' was not found. Did you type it correctly?"
          "\nRun script again and try again.")
    exit()

# The user wants to encrypt. Build an encrypted file.
if action == "e":
    # Do some encrypting of information
    infile_header = str(encrypt(in_file, PASSWORD)).replace(", ", " ").strip("[").strip("]") + "::"
    extension = str(encrypt(".txt", PASSWORD)).replace(", ", " ").strip("[").strip("]") + "\n"
    encoded_message = encrypt(input_file, PASSWORD)
    # Open an output file and write the encrypted information
    output = open("encoded_output.txt", "w+")
    print("Writing file header and metadata...")
    output.write(HEADER + infile_header + SOURCE + ENCODED + extension)
    print("Writing file contents to output in encoded form...")
    output.write("".join(str(encoded_message).replace(", ", " ").strip("[").strip("]")))
    
# The user wants to decrypt so decrypt the file they provided
elif action == "d":
    # Conditon the encrypted file and split the input file by it's delimter (::)
    temp_file_list = input_file.strip("#DEC_ENC").replace('\n', "::").split("::")
    # Remove empty list items
    file_list = filter(None, temp_file_list)
    # Find the password
    solved_password = find_password(file_list)
    # Decode the output (Some is encrypted with the "empty" password)
    file_note = decrypt(file_list[0].split(), PASSWORD)
    file_source = decrypt(file_list[1].split(), PASSWORD)
    file_contents = decrypt(file_list[4].split(), solved_password)
    # Open the output file and write the decrypyed information
    output = open("decrypted_output.txt", "w+")
    output.write("".join(file_note) + "\n" + "".join(file_source) + "\n" + "".join(file_contents))
    print("Output written to file: decrypted_output.txt")
