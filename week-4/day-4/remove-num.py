a=[56,43,21,58,99,113,99,99,99]

while True:
    c=a.count(99)
    if c==0:
        break
    a.remove(99)

print(a)