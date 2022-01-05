def hashcode(key):

    hash = len(key)

    return hash

def main():

    keyList = ['hi', 'abc', 'pword']

    hashcodeList = []

    for element in keyList:
        if hashcode(element) in hashcodeList:
            print("Old hashcode")
            hashcodeList[hashcode(element)].append(element)
        else:
            print("New hashcode")
            hashcodeList[hashcode(element)].append(element)
    
    print(hashcodeList)

if __name__ == "__main__":
    main()