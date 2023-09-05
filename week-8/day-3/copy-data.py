"""
Function copydata
"""
old=input("enter old file name: " )
new=input("enter new file name: ")

def copyData(old,new):
    with open(f"{old}.txt","r") as f:
        value=f.readlines()
        print(value)
    with open(f"{new}.txt","w")as f:
        for i in value:
            f.write(i)
copyData(old,new)

