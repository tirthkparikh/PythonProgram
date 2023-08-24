def primeNumber():
    num = int(input("Enter num= "))
    count = 0
    for i in range(1,num+1):
    
        if num % i == 0:
            count = count + 1
            
            
    if count == 2:
        print("it is a prime num")
    else:
        print("it is not a prime num")



primeNumber()



