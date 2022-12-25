#object
a = 5
isinstance(a,object)

def func():
    pass
type(func)

class A:
    name = "asif"
    marks = 100
    
type(int)

class A:
    def__call__(self):
        print("call me")
        
func.__call__()

a = ("name")

a.__getiton__("name")


class A:
    def__init__(self):
        print("A init executed")
        
class B:
    def __init__(self):
        print("B init executed")
        
abc = B()

#super is a key word

classB(A):
    
#MRO (Method Resolution Order)
class A:
    pass
class B(A):
    x = 5 
class C(B):
    pass
class D(A):
    x = 10
classE(C,D):
    pass

#Iteration protocal
a = range(5)
it = a.__iter__()

next(it)

#GENERATORS

a = []
for i in (range,100):
    a.append()
    
def generate_squares(n):
    return [i**2 for i in range (1,n)]

for x in generate(1, 100000000)

#yield is a key word
 def generate_squares(n):
     for i in range(1,n):
         yield i**2
         
for i in generate_squares(10):
    
def func():
    print("start")
    yield 1 
    print("yielded 1 ")
    yield 2 
    print("yielded 2 ")
    
print("hello")
it = iter(func())
next(it)

a = (i **2 for i in range(10) )
for i in a :
    print(a)
    
