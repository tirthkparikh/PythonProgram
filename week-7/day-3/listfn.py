
def sum1(a:list)->str:
       
        return prime(sum(a))

def prime(a:int)->str:
    for i in range(2,int(a**1/2)):
        if a%i==0:
            return "Not-prime"
    return "Prime"
print(sum1([2,2,3]))
