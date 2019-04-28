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
    ret = []
    base_header = encrypt("ENCODED", 0)
    encrypted_header = data[2].split()
    for l in range(len(encrypted_header)):
        encrypted_header[l] = int(encrypted_header[l])
        password_test = int(encrypted_header[l]) - int(str(base_header[l]))
        ret.append(str(password_test))
    for k in range(len(ret)):
        if ret[0] == ret[k]:
            pass
        else:
            print("Passwords do not match!")
            quit()
    encoded_header = encrypt("ENCODED", int(ret[0]))
    for j in range(len(encoded_header)):
        if encoded_header[j] == encrypted_header[j]:
            print("Found valid password! Attempting to decrypt file...")
            return int(ret[0])
        else:
            print("Password not valid... Quiting program. Output: \n" + str(encoded_header) + "\n" + str(encrypted_header))
            quit()


def ask():
    ask1 = input("Would you like to encode or decode a file Choices: e or d: ")
    if ask1 != "e" and ask1 != "d":
        print("Invalid option. Please try again!")
        ask()
    ask2 = input('What is the name of the file you wish to use? (".txt" only. Exclude file format from response): ')
    return ask1, ask2


MaxValue = 65534
password = 5886
test = ask()
infile = test[1]

if test[0] == "e":
    header = "#DEC_ENC::"
    encoded = str(encrypt("ENCODED", password)).replace(", ", " ").strip("[").strip("]") + "::"
    source = str(encrypt("Colin's Encoder", password)).replace(", ", " ").strip("[").strip("]") + "::"
    infile_header = str(encrypt(infile, password)).replace(", ", " ").strip("[").strip("]") + "::"
    extension = str(encrypt(".txt", password)).replace(", ", " ").strip("[").strip("]") + "\n"
    with open(infile + ".txt", "r") as r:
        file = r.read()
    encoded_message = encrypt(file, password)
    output = open("encoded_output.txt", "w+")
    output.write(header + infile_header + source + encoded + extension)
    print("Writing file header and metadata...")
    output.write("".join(str(encoded_message).replace(", ", " ").strip("[").strip("]")))
    print("Writing file contents to output in encoded form...")

elif test[0] == "d":
    try:
        with open(infile + ".txt", "r") as r:
            file = r.read()
    except FileNotFoundError:
        print("Error opening file: {}. Did you type the name correct and exclude the file format?".format(infile))
        ask()
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
