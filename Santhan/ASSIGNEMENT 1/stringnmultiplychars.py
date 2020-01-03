
def stringMultiply(str):
    res = ''

    # increment by 2 over iterations
    for i in range(0, len(str), 2):

        # casting every second charcter
        num = int(str[i+1])

        # adding up char n times to result
        for j in range(num):
            res += str[i]

    return sorted(res)

# test 1
print(stringMultiply("c4b3g6h1"))

# test 2
print(stringMultiply("f4g5c2n6o2"))