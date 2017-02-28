#!/usr/bin/env python 

# First program
print "Hello world!"
# raw_input()

string = "Cadena"
integer = 3
long_int = 4L 
exa = 0x12
real = 0.1e-3
complejo = 2.3+7.8j  

# check the type
print type(string) 
print type(integer)
print type(long_int)
print type(exa)
print type(real)
print type(complejo)

# Operators
divicion = complejo / integer 
divicion_entera = complejo // integer
exponente = integer ** integer
_and = 3 & 2 
print divicion
print divicion_entera
print exponente
print _and

# Strings
unicode_str = u"unicode string"
raw = r"\n"

print unicode_str
print raw 
# concatenations
print raw * 3
print raw + raw
print raw , raw

# Lists
l = [3, 4.5, 'dog', [1,2]]
print l
# get the last element
print l[-1]
# get a range of elements with step
print l[0:4:2]
print l[:2]
print l[2:]
print l[::2]

# Tuples
t = (1, 2, True, 'python')
t2 = (1,)
print type(t2)

# Dicctionarys
d = {"Peter": "Pan", "us": "the best country"}
print d["us"]
print d.keys()
print d.values()

# Functions
def my_function(a,b=1):
    """ This function power a to b and print the result
    """
    print a**b
my_function(2,3)
# changing the order
my_function(b=2, a=3)
# params by default
my_function(3)
# with variable amount of params
def my_sum(a,b,*others):
    ret = a + b
    for i in others:
        ret += i
    return ret

print my_sum(1,2)
print my_sum(1,2,3)
print my_sum(1,2,3,4)

# with variable amount of params as a dicctionary
def my_sum(a,b,**others):
    ret = a + b
    for i in others.keys():
        ret += others[i]
    return ret

print my_sum(1,2)
print my_sum(1,2, tercero = 3)
print my_sum(1, 2, tercero = 2, cuarto = 4)

# Returning tuples
def point_mul_two(x,y):
    return x*2, y*2
print point_mul_two(3,4)

# Object Oriented Programming (OOP) with new style
class Person:
    """This is a person"""
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age

class Graduate:
    """This is something graduated from College"""
    def __init__(self, p_college):
        self.college = p_college

class Employee(Person,Graduate,object):    
    """This is an Employee"""
    def __init__(self,p_name, p_age, p_salary, p_college):
        Person.__init__(self, p_name, p_age)
        Graduate.__init__(self,p_college)
        self.salary = p_salary
    
    def getSSN(self):
        return self.__ssn
    def setSSN(self, p_ssn):
        if str(p_ssn).count == 9:
            self.__ssn = p_ssn
        else:
            print "ERROR" 
    ssn = property(getSSN, setSSN)

empl = Employee("Peter", 12, 70000, "UCI")
empl.ssn = '1234567890'

# Functional programming
def is_par(a):
    return a % 2 == 0
def my_sum2(a,b):
    return a+b

# map(func, list)
l = map(str, [1,2,3,4,5])
print l

# reduce(func, list)
l = reduce(my_sum2, [1,2,3,4,5])
print l

# filter
l = filter(is_par, [1,2,3,4,5])
print l

# lambda
l = map(lambda x: str(x), [1,2,3,4,5])
print l

# list comprehension
l = [(x,y) for x in range(1,20,1) for y in range(2,20,2) if x*y % 2 == 0]
print l

# Generators
for i in (n ** 2 for n in range(10)):
    print i

# Decorators
def function_name(fun):
    def nueva(*args):
        print "Function name: ", fun.__name__
        return fun(*args)
    return nueva

@function_name
def multiplica(a,b):
    return a * b

print multiplica(2,3)

# Exceptions
try:
    a = 1
    b = 0
    c = 0
    if b == 0:
        raise ZeroDivisionError()
    else:
        c = a / b
except ZeroDivisionError:
    print "Zero divicion is not permited"
finally:
    print "Cleaning"





