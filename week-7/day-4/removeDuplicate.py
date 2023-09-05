def removeDuplicate(a:list)->list:
    # b=[]
    # for i in a:
    #     if b.count(i)<1:
    #         b.append(i)
    for i in a:
        while True:
            c=a.count(i)
            if c==1:
                break
            a.remove(i)


    return a
c=removeDuplicate([1,2,33,4,5,33,4,5,55,5])
print(c)