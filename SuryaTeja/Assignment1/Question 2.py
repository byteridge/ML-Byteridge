str = input("Enter the string: ")
temp = str[0]
print(temp)
flag = 1
for v in str:
    for t in temp:
        if v == t:
            flag = 0
    if flag == 1:
        print(v)
        temp = temp + v
    else:
        flag = 1
