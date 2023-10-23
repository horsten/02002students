a = 3
b = 7
tmp = a
a = b
b = tmp
print("a="+str(a)+", b="+str(b))

a = 3
b = 7
a, b = b, a
print("a="+str(a)+", b="+str(b))

