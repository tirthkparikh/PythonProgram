arr=["hi" for i in range(1,31)]
arr=[item for item in range(1,30) if item%2==0]
def checkPrime(num:int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


# a = [i for i in range(1, 31) if checkPrime(i) == True]
a = [i for i in range(1, 31) if checkPrime(i)]

print(a)
print(arr)
