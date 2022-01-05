def checkPerm(x, y):

    dict = {}

    for letter in x:
        letter = letter.lower()
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    for letter in y:
        letter = letter.lower()
        if letter in dict:
            dict[letter] -= 1
    
    for value in dict:
        if dict[value] != 0:
            return False
        else:
            return True

def main():

    x = input("First String: ")
    y = input("Second String: ")

    trueOrFalse = checkPerm(x, y)
    
    if trueOrFalse:
        print(f'Both the strings, {x} and {y}, are permutations of one another')
    else:
        print(f'Both the strings, {x} and {y}, are not permutations of one another')

    # To make the problem case sensitive, you can make lowercase each letter before assigning them as a key

if __name__ == "__main__":
    main()