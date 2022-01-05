def isUnique(string):

    dictionary = {}

    if string == "":
        return True
    for letter in string:
        if letter in dictionary:
            return False
        else:
            dictionary[letter] = 1
    return True

def isUniqueNoDS(string):
    for i in range(0, len(string) - 1):
        currentChar = string[i]
        print(f'Current Char {currentChar}')
        for j in range(i+1, len(string)):
            nextChar = string[j]
            print(f'Next Char {nextChar}')
            if currentChar == nextChar:
                print(f'Same character!')
                return False
    return True


def main():

    string = input("Input: ")
    choice = input("1: Uses Datastructure / 2: No Datastructure => : ")

    # trueOrFalse = isUnique(string)

    if choice == "1":
        trueOrFalse = isUnique(string)
    else:
        trueOrFalse = isUniqueNoDS(string)

    if trueOrFalse:
        print(f'String: {string} is unique')
    else:
        print(f'String: {string} is not unique')

   

if __name__ == "__main__":
    main()

# IS Unique
# Implement an algorithm if a string has all unique chracters
# First identify whether or not the string is in ASCII string or Unicode string.
# Assuming ASCII we can now identify some edge cases.
# String cannot be greater than 128 characters. This is due to the fact ASCII has only 128 characters thus the longest possible unique string would have to contain every single existing
# character in the ASCII alphabet to be still considered unique.
# Assuming we are solving this in Python, we can make use of a dictionary as we iterate through the entirety of our string that generates keys for each character that we identify. 
# While iterating, if we do find that the generated key already exists in our dictionary than we know that the character in question has already been seen thus eliminating the word
# as a unique character. For other languages such as Java and C++ we cna make use of Hash Tables in a similar fashion to help us identify duplicate characters.
# We can also make use of set() if solving in Python. It can be time consuming and inefficient if the string is quite massive. 