a=[100,200,300]
b=a
a.append(100)
print(id(a),id(b))
print(a,b)
# above method will change both arrays to avoid it we do a.copy(\)

c=7
d=c
c+=1
# here we reasssign c so it's memory location will change
print(id(c),id(d))
print(c,d)