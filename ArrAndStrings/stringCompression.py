def stringCompression(string):

    if string is None:
        return string
    else:
        currentLetter = string[0]
        compressedString = ""
        increment = 0
        lettersTraversed = 0
        for letter in string:
            if currentLetter != letter:
                compressedString += currentLetter
                compressedString += str(increment)
                currentLetter = letter
                increment = 0
            increment += 1
            lettersTraversed += 1
            if lettersTraversed == len(string):
                compressedString += currentLetter
                compressedString += str(increment)
        if len(compressedString) > len(string):
            return string
        else:
            return compressedString


    
def main():

    stringInput = input("String to be compressed: ")
    
    output = stringCompression(stringInput)

    print(output)

if __name__ == "__main__":
    main()