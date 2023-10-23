import math

def ex(name):
    print("\nExercise "+name+"\n"+(len(name)+9)*"="+"\n")

def print_var(name, var):
    print("Variable "+name+" is of type "+type(var).__name__+" and has value "+str(var))

def irfc(name, var):
    print_var(name, k)
    print("int("+name+"): "+str(int(var)))
    print("round("+name+"): "+str(round(var)))
    print("math.floor("+name+"): "+str(math.floor(var)))
    print("math.ceil("+name+"): "+str(math.ceil(var)))    

ex("1.6a")
k = 16.2
irfc("k", k)

ex("1.6b")
k = 16.8
irfc("k", k)

ex("1.6c")
k = -16.2
irfc("k", k)

ex("1.6d")
k = -16.8
irfc("k", k)

ex("1.6e")
x = 2
print_var("x", x)
print("abs(x): "+str(abs(x)))
print("math.sqrt(x): "+str(math.sqrt(x)))
print("math.pow(x,2): "+str(math.pow(x,2)))


ex("1.6f")
a = 12
b = 7
print(a + b)
print(a % b) # remainder of a/b (modulus)
print(a / b)
print(a // b) # what is the difference between / and //?
# // is floor division ignoring remainder
print(max(a, b))
print(a < b)
print (a==b)

ex("1.6g")
a = True
b = False
print(a and b)
print(a or b)

ex("1.6h")
a = 4
b = 8
c = 72
print((a < c) and (b < c))
print((a < c) or (a == b))

ex("1.6i")
a = 8
b = 12
x = '6'
y = ' years'
print(a + b)
#print(a + y) # why does this give an error? - Unsupported operand types for + int and str
print(x + y)
print(str(a) + y)
