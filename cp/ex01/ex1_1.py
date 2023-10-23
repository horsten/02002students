def ex(name):
    print("\nExercise "+name+"\n"+(len(name)+9)*"="+"\n")

def print_var(name, var):
    print ("Variable "+name+" is of type "+type(var).__name__+" and has value "+str(var))

ex("1.1a")
b = 10
b = b - 5
b = 2 * (b - 5)
print_var("b", b)

ex("1.1b")
q = 14
q = q - 4
q = 0.5 * (q + 2)
print_var("q", q)

ex("1.1c")
k = 20
k = k/2
k = 3 * (k -5)
print_var("k", k)

ex("1.1d")
a = 15.5
b = a
a = 7
print_var("a", a)
print_var("b", b)

ex("1.1e")
a = 5
b = 3
a = b
b = a
print_var("a", a)
print_var("b", b)

ex("1.1f")
this = 15
this = 'that'
print_var("this", this)

ex("1.1g")
i = 15
i = 1 + 1
i = i + 1
print_var("i", i)

ex("1.1h")
letters = 'abc'
letters = letters + 'x'
letters = letters + 'y'
print_var("letters", letters)

ex("1.1i")
test = 'test'
test = 2 * test + 'no'
print_var("test", test)

ex("1.1j")
day = 15
valid = day>0 and day<32
print_var("day", day)
print_var("valid", valid)

ex("1.1k")
name = 'Filip'
age = 12
c = name * age
print_var("name", name)
print_var("age", age)
print_var("c", c)
