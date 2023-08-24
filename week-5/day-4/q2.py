a = "Aeroplane is the best mode of travel"

# travel of mode best the is Aeroplane
# enalporeA si eht tseb edom fo 

# levart fo edom tseb eht si enalporeA

b=a.split()
c=b[::-1]
print(" ".join(i for i in c))

b=a.split()
c=[]
for i in b:
    c.append(i[::-1])
print(" ".join(i for i in c))

b=a.split()
c=b[::-1]
d=[]
for i in c:
    d.append(i[::-1])

print(" ".join(i for i in d))

