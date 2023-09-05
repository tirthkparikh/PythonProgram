f=open("hi.txt","r")
lines=f.readlines()
print(lines)
for line in lines[::-1]:
    print(line.strip())
