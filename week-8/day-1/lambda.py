# def add(num1, num2):
#     #...
#     return num1 + num2

# Lambda/Anonymous function
add = lambda x, y: x + y
generateEvenList = lambda start, end: [i for i in range(start, end + 1) if i % 2 == 0]

print(add(10, 20))
print(generateEvenList(4, 20))