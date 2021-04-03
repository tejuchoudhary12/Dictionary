list1 = [1,2,3,1,2,3,4,1,2,3,4,5]

f = {}
for i in list1:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

print(f)
