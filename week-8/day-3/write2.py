name=input("Enter your name: " )
age=int(input("enter your age: "))
gender=input("enter your gender: ")[0]

def makeFile(name:str,age:int,gender:str):

    f=open(f"{name}.txt","w")
    f.write(f"My name is {name}\n")
    f.write(f"My gender is {gender}\n")
    f.write(f"My age is {age}")
    f.close()

makeFile(name,age,gender)
    
