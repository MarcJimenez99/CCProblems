def oneReplacement(string1, string2):

    if len(string1) != len(string2):
        return False
    else:
        i = 0
        numDiff = 0
        for letter in string1:
            if string1[i] != string2[i]:
                numDiff += 1
            i += 1
        if numDiff > 1:
            return False
        else:
            return True    

def oneInsertionRemoval(string1, string2):

    if len(string1) > len(string2):
        return False
    else:
        index1 = 0
        index2 = 0
        # Track both indexes seperately to identify where the two
        # strings diverge.
        while index1 < len(string1) and index2 < len(string2):
            # Iterate through entirety of both strings
            if string1[index1] != string2[index2]:
                # If letters do not match at current indicies check:
                if index1 != index2:
                    # If index1 != index2 it's because we've already found
                    # a discrepancy in both strings. Since we are looking
                    # for single edits, they're can't be two areas where 
                    # the two strings are different
                    return False
                # If its the first discrepancy then index1 should equal index2
                # so we will just increment the second index to check whether
                # or not the rest of the string is accurate
                index2 += 1
            else:
                # If letters do match than iterate both indexes
                index1 += 1
                index2 += 1
        return True    

def main():

    string1 = input("string1: ")

    string2 = input("string2: ")
    sameString = False
    if string1 == string2:
        sameString = True
    
    oneReplacementCheck = oneReplacement(string1, string2)
    oneInsertionCheck = oneInsertionRemoval(string1, string2)
    oneRemovalCheck = oneInsertionRemoval(string2, string1)
    # We will use the same function to check insertion and removal since 
    # removal is just the inverse of insertion. Thus we will just swap both strings.
    if oneReplacementCheck or oneInsertionCheck or oneRemovalCheck or sameString:
        print(f'{string1} and {string2} are one insert/remove/replace a character away from one another')
    else:
        print(f'{string1} and {string2} are not one insert/remove/replace a character away from one another')

if __name__ == "__main__":
    main()