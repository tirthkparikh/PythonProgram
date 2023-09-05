from timeit import timeit

print("hi")
def generateList():
    a = []
    for i in range(1, 10):
        a.append(i)
    return a
print("hi")


def generateList2():
    return [i for i in range(1, 10)]
print("hi")


t1 = timeit(stmt=generateList)
print("hi")
t2 = timeit(stmt=generateList2)

print(t1)
print(t2)