x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(x.items())
r = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
print(r)
x=[1,2,[3.4]]
y=[3,4]
x+=y
print(x)


def flatten_list(n):
    final = []
    count=0
    for i in n:
        count+=1
        print(n,len(n),count)
        if type(i) == list:
            n +=i
            # print(id(n))
        else:
            final.append(i)
        # print(n)
    b = sorted(final)
    return b

# def flatten_list(n):
#     final = []

#     for i in n:
#         if type(i) == list:
#             n = n+i
#         else:
#             final.append(i)
#     b = sorted(final)
#     return b

nested_list_1 = [1, [2, 3, [4, 5]], 6, [7, 8]]
# nested_list_2 = [1, [2, [3, [4, [5]]]]]
# nested_list_3 = [1, 2, 3, 4, 5]
print(flatten_list(nested_list_1))
# print(flatten_list(nested_list_2))
# print(flatten_list(nested_list_3))

