data=input("enter your data: ")
name=input("enter your filename: ")

with open(f"{name}.txt","w") as f:
    f.write(data)

