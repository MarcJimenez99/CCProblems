def isPalindromePermutation(string):
    lengthOfString = len(string)
    dict = {}
  
    for letter in string:
        letter = letter.lower()
        if letter in dict:
            dict[letter] += 1
        else:
            if letter != " ":
                dict[letter] = 1
            else:
                lengthOfString -= 1

    if lengthOfString % 2 == 0:
        for value in dict:
            if (dict[value] % 2) != 0:
                return False
        return True
    else:
        counter = 0
        for value in dict:
            if (dict[value] % 2) != 0:
                if counter == 1:
                    return False
                else:
                    counter += 1
        return True
            
    

def main():

    string = input("Input: ")

    isPalindrome = isPalindromePermutation(string)
   
    if isPalindrome:
        print(f'{isPalindrome}')
        print(f'String: {string} is a permutation of a palindrome')
    else:
        print(f'{isPalindrome}')
        print(f'String: {string} is not a permutation of a palindrome')

if __name__ == "__main__":
    main()