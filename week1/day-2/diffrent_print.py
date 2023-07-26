"""
diffrent ways to print variable 
int(%d),str(%s),bool(%),float(%f)
"""
a = 23
b = 2.5
c = "tirth"
d = False

# method-1 normal print by , // , gives space
print("My name is", c)
print("My name is", c, "my age is", a)

# method-2 f-string method we can add varibale in {} by using f
print(f"my name is {c} and my age is {a}")

# method-3 by%
# remember sequence is imp
print("My name is %s and My age is %d" % (c, a))
