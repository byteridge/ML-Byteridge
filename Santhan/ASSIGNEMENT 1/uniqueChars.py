

def uniqueChars(str):
    res = ''

    for i in range(0, len(str)):

        # char at 0 will be there regardless
        if(i == 0):
            res+= str[i]

        # checking if char exist in result string & adding
        if(str[i] not in res):
            res += str[i]

    return res

# test 1
print(uniqueChars("malayalam"))

