from random import choice

class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age
    def __str__(self):
        return "" + str(self.name)
    

person_list = [Person(p_name = "Name %s" % str(i), p_age = choice(range(30))) for i in range(10)]        

person_list.sort(key=lambda x: x.age, reverse=False)

can_drive = filter(lambda x: x > 21, map(lambda x: x.age, person_list))

person_str = ["%s - %s" % (p.name, p.age) for p in person_list]

list_ages = lambda z: z.age

def sum(x,y):
    return x+y


total_age = reduce(sum, map(lambda x: x.age, person_list))

numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

numbers_letters = [i + j for i in letters for j in letters]

def function_name(fun):
    def nueva(*args):
        print "Function: ", fun.__name__
        return fun(*args)
    return nueva

@function_name
def multiplica(a,b):
    return a * b

#print person_list
print total_age
print can_drive
print person_str
print numbers_letters 
print multiplica(2,3)



