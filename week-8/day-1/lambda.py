# def add(num1, num2):
#     #...
#     return num1 + num2

# Lambda/Anonymous function
add = lambda x, y: x + y
generateEvenList = lambda start, end: [i for i in range(start, end + 1) if i % 2 == 0]

print(add(10, 20))
print(generateEvenList(4, 20))

x=[1,2,34,56,77]
filterList= lambda x: [item for item in x if item%2==0]
squareANum = lambda item : item**2
print(squareANum(4))
print(filterList(x))
y=[(1,5),(3,2),(2,8),(1,3)]
y.sort(key = lambda item:item[1],reverse=True)
print(y)
i=[1,2,3,4,5]
