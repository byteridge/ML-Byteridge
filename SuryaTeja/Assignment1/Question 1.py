str = input('Enter the pattern: ')
flag = 1
a = ''
n = ''
f = ''
i = 0
j = 0
out = ''
for s in str:
    if flag == 1:
        a = a + s
        flag = 0
    else:
        n = n + s
        flag = 1
while i<len(a):
    while j < int(n[i]):
        f = f + a[i]
        j += 1
    i += 1
    j = 0
d = sorted(f)
for k in d:
    out = out + k
print(out)
