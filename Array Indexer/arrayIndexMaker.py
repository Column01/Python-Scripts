outputFile = "outputFile.txt"
inputFile = "inputArray.txt"
try:
    arr = open(inputFile, "r").read().strip("\n").strip("[").strip("]").strip(',').split(",")
    output = open(outputFile, "w+")
    for i in range(len(arr)):
        output.write("arr[{}] = {}\n".format(i, arr[i]))
except FileNotFoundError:
    print("inputArray.txt does not exist. Please make a file and put an array inside it!")
