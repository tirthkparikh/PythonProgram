f=open("hello.txt","r")
data=f.read().lower()
count=0
for i in data:
    if i == "o":
        count+=1
print(count)
f.close()
