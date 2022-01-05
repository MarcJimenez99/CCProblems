# def URLify(string, strLength):
    
#     newString = ""
#     counter = 0
    
#     while counter != strLength:
#         letter = string[counter]
#         if letter != " ":
#             newString += letter
#         else:
#             newString += "%20"
#         counter += 1
#     return newString

def URLify(string, trueStrLength):
    
    numberOfSpaces = (len(string) - trueStrLength) / 2

    trueStrIter = trueStrLength - 1
    strIter = len(string) - 1
    stringList = list(string)
    while trueStrIter >= 0:
        if stringList[trueStrIter] != " ":
            stringList[strIter] = stringList[trueStrIter]
            strIter -= 1
        else:
            stringList[strIter] = "0"
            stringList[strIter-1] = "2"
            stringList[strIter-2] = "%"
            strIter -= 3
        trueStrIter -= 1
    
    string = ''.join(stringList)
    return string
def main():

    # Assumes that the trailing whitespace will always be enough to fulfill the inserted special characters
    string = "Mr John Smith    "
    trueStrLength = 13

    # newString = URLify(string, len(string))
    string = URLify(string, trueStrLength)

    print(string)

    # print(f'String: {string}')
    # print(f'URLifyed String: {newString}')

if __name__ == "__main__":
    main()

# URLify 
# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold 
# the additional characters, and that you are given the "true" 
# length of the string. 
# (Note: if implementing in Java, please use a character array 
# so that you can 
# perform this operation in place.) 
#
# Are inputs are given as the unedited string that includes trailing
# white space and then the integer number that represents the true length
# of our string.  
#
# So since we are given the true length of our string and we know the unedited
# string has trailing white space in order to accomodate the insertion
# of '%20' for each white space, we can identify how many white spaces
# exist in our string by subtracting the total length of the unedited string
# and the true length. 
#
# Next we are going to set up two iteration integers that will help us
# iterate backwards through our string both at the end of the unedited
# string and at the last character of the true string. In addition we are
# going to change our string into a list allowing us to physically make 
# changes to it at each character. 
#
# Now we are going to iterate from the last character until we get to the
# beginning of our string. At each character if we find that the character is
# not a space we are then going to insert it at our iteration integer 
# at the end of the string and then subtract our iteration integer by 1.
# Else, if it is a space, we are going to insert '%20' and subtract our
# iteration integer by 3, or the length of '%20'. In both cases we will
# also subtract our trueStringIteration integer by 1.
# 
# Finally we will use ''.join() to join our string list into a string
# again, and return it. 
#
# If we were not to create a list, we can instead return a new string 
# where we would just iterate from the beginning and read each character
# and append to our new string each time.