def total():
    with open("total.txt","r") as f:
        data=f.readlines()
        total=0
        for i in data:
            total+=int(i)
    print(total)
total()