"""
delete fn - del a[o] : delte number at oth index in list
del a : delete whole variable

a.pop(): remvoes last value from list
a.pop(i): removes ith index element from list

a.remvoe(value): takes one arugment by default , also removes the value's first ocurence in list
"""
a = [22, 54, 65, 76, 564, 43, 11]
del a[1]
print(a)
a.pop()
print(a)
a.pop(3)
print(a)
a.remove(564)