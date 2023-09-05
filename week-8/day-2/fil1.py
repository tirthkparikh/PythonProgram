f=open("hi.txt","r")
lines=f.readlines()
print(lines)
for line in lines:
    a=line.strip().split()[::-1]
    b=(" ").join(item for item in a)
    print(b)
f.close()