a=[56,43,21,58,99,113]

small=a[0]
for i in range(len(a)):
    if a[i]<small:
        small=a[i]
print(small)