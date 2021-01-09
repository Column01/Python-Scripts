input_file = input("Please enter the name of your file that contains the array (include the extension!): ")
if input_file is None or isinstance(input_file, int):
    print("Invalid input file.")

try:
    arr = open(input_file, "r").read().strip("\n").strip("[").strip("]").split(",")
    if len(arr) == 0:
        print("Unable to parse an array from the input file. Make sure it looks like this: [1, 2, 3, 4]")
        exit()

    output = open("output.txt", "w+")
    for i in range(len(arr)):
        output.write("arr[{}] = {}\n".format(i, arr[i]))
    print("Array has been indexed and placed in a file called \"output.txt\"")
except FileNotFoundError:
    print("{} does not exist. Please make a file and put an array inside it!".format(input_file))
