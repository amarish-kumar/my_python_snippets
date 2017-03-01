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

# Regular Expresions
import re 
if re.match("python","python"):
    print "python", "matchea con", "python"
# 1 character followed by ython
if re.match(".ython","python"):
    print "ython", "matchea con", "python"
if re.match(".ython","cython"):
    print "ython", "matchea con", "cython"
# 3 characters followed by a point
if re.match("...\.","abc."):
    print "...\.", "matchea con", "abc."
if re.match("(p|c|j)ython","python"):
    print "(p|c|j)ython", "matchea con", "python"
if re.match("[pcj]ython","python"):
    print "([pcj]ython", "matchea con", "python"
# python followed by a digit 
if re.match("python[0-9]","python0"):
    print "(python[0-9]", "matchea con", "python0"
# python followed by a digit or letter or upper letter
if re.match("python[0-9a-zA-Z]","pythonY"):
    print "(python[0-9a-zA-Z]", "matchea con", "pythonY"
# python followed by something different of a lower letter o digit 
if re.match("python[^0-9a-z]","pythonY"):
    print "(python[^0-9a-z]", "matchea con", "pythonY"
# a digit
if re.match("python[\d]","python6"):
    print "(python[\d]", "matchea con", "python6"
# a non-digit
if re.match("python[\D]","pythonA"):
    print "(python[\D]", "matchea con", "pythonA"
# a alpha-numeric character
if re.match("python[\w]","python8"):
    print "(python[\w]", "matchea con", "python8"
# a non-alpha-numeric character
if re.match("python[\W]","python-"):
    print "(python[\W]", "matchea con", "python-"
# a blank character
if re.match("python[\s]","python "):
    print "(python[\s]", "matchea con", "python "
# a non-blank character
if re.match("python[\S]","python0"):
    print "(python[\S]", "matchea con", "python0"
# 1 or more than 1 ocurrencies
if re.match("python+","pythonnn"):
    print "python+", "matchea con", "pythonnn"
# 0 or more than 1 ocurrencies
if re.match("python*","pytho"):
    print "python*", "matchea con", "pytho"
# n has to appear between 3 and 8 times
if re.match("python{3,8}","pythonnnnnn"):
    print "python{3,8}", "matchea con", "pythonnnnnn"
# start with http
if re.match("^http","http://python.com"):
    print "^http", "matchea con", "http://python.com"
# end with .com
if re.match("\com$","http://python.com"):
    print ".com$", "matchea con", "http://python.com"

# Sockets
import socket

# server-side
sock_server = socket.socket()
sock_server.bind(("localhost",9999))
sock_server.listen(10)

sock_c, addr = sock_server.accept()

while True:
    text = sock_c.recv(1024)
    if text == "quit":
        break
    print "Recived:", text
    sock_c.send(text)

print "bye!"
sock_c.close()
sock_server.close()

# client-side
sock_client = socket.socket()
sock_client.connect(("localhost",9999))

while True:
    text = raw_input("> ")
    if text == "quit":
        break
    sock_client.send(text)

print "bye!"
sock_client.close()

# Interacting with WEBS

import urllib2, urllib

def download_progress(count, block_size, total_size):
    print "Percent downloaded: %d " % int(count * blockSize * 100 / totalSize)

try:
    params = urllib.urlencode({
        "user": "jonh",
        "password": "passW0rd!" 
    })
    # POST
    f = urllib2.urlopen("http://www.pyhton.org/", params)
    # GET
    f2 = urllib2.urlopen("http://www.pyhton.org/" + "?" + params)
    # DOWNLOAD
    f3 = urllib.urlretrieve("http://www.pyhton.org/file.zip","file.zip",reporthook=download_progress)

    # Using Request
    ua = "Mozilla/5.0 (compatible; Konqueror/3.5.8; Linux)"
    h = {"User-Agent": ua} 
    r = urllib2.Request("http://www.python.org", headers=h) 
    f4 = urllib2.urlopen(r) 

    print f.read()
    f.close()
    f2.close()
    f3.close()
    f4.close()
except HTTPError as e:
    print "ERROR: ", e.code
except URLError as e:
    print "ERROR: ", e.reason


 


