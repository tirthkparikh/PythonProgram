a = [22, 54, 65, 76, 564, 43, 11]
num =int(input("Ask number from user: "))
pos =int(input("Ask position from user: "))

if pos>len(a):
    print("poisition is grater than length of list")
else:
    a.insert(pos,num)
    print(a)