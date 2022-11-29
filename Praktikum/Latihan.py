import math

def a(x):
    return x**2
a = lambda x: x ** 2
print(a(46))

def b (x,y):
    return math.sqrt(x**2 + y**2)
b = lambda x,y: x**2 + y**2
print(b(4,6))

def c (*args):
    return sum(args)/len(args)
c = lambda *args : sum(args)/len(args)
print(c(5,7,9,11,10))

def d(s):
    return "".join(set(s))
d = lambda s: "".join(set(s))
print(d("Tertimpa"))