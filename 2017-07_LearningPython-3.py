# Python 3 Essential Training - Bill Weinman _ Lynda.com

print ("Hello, World!")

a,b = 5,1
if a < b:
	print('a ({}) is less than b ({})' .format(a,b))
else:
	print('a ({}) is not less than b ({})' .format(a,b))

print("foo" if a < b else "bar")


# simple fibonacci series - the sum of two elements defines the next set

a,b = 0,1
while b < 50:
	print(b)
	a, b=b, a+b
print("Done.") # if indented will be part of loop

# read the lines from the file

fh = open("lines.txt")
for line in fh.readlines():
	print(line)


# Function

def isprime(n):
	if n == 1:
		print("1 is special")
		return False
	for x in range(2,n):
		if n % x == 0:
			print("{} equals {} x {}" .format(n, x, n // x))
			return False
	else:
		print(n, "is a prime number")
		return True

for n in range (1,20):
	isprime(n)


# Generator 

def isprime(n):
	if n == 1:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
	else:
		return True

def primes(n=1):
	while(True):
		if isprime(n): yield n
		n += 1
			# "yield" returns a value, and the next time the function is called, it continues execution after the yield
			# It checks to see if the number is prime. If it's not, it increments and checks the next one. 
			# If it is, it yields. And that will return a value. 
			# Then the next time this function is called, it'll just continue here, incrementing and looking for the next one. 
			# Because of these of yield, it returns an iterator object, that is suitable for use in a for loop.


for n in primes():
	if n > 100: break
	print(n)


# simple fibonacci series 
class Fibonacci():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def series(self):
		while(True):
			yield(self.b)
			self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break    
    print(r)


class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has gray and white feathers.",
        bark = "The duck cannot bark.",
        fur = "The duck has no fur."
    )
 
class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        feathers = "The dog has no feathers.",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
 
def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest:")
    for o in ( donald, john, fido ):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in ( donald, john, fido ):
        in_the_doghouse(o)
 
if __name__ == "__main__": main()


# Refined version 

class AnimalActions:
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')

    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()

# -- MODEL -- 

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has gray and white feathers."
    )
 
class Person(AnimalActions):
    strings = dict(
        bark = "The person says woof!",
        fur = "The person puts on a fur coat.",
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it."
    )

class Dog(AnimalActions):
    strings = dict(
        bark = "Arf!",
        fur = "The dog has white fur with black spots.",
    )

# -- CONTROLLER -- 

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
 
def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("-- In the forest:")
    for o in ( donald, john, fido ):
        in_the_forest(o)

    print("-- In the doghouse:")
    for o in ( donald, john, fido ):
        in_the_doghouse(o)
 
if __name__ == "__main__": main()


# Exceptions 

try: 
	fh = open('xlines.txt')
	for line in fh.readlines():
	    print(line)

except IOError as e:
	print("something bad happened ({})" .format(e))

print("after badness")


## Creating a main script

#!/usr/bin/python3
	# path to the Python interpreter

def main(): print("This is the syntax.py file.")

if __name__ == "__main__": main()
	# Run script with functions in any order desired 
	# Allows functions to be defined after they are called 
# If only one line of code in a particular structure, it can be on the same line


# Conditional expressions 

def main():
	a,b = 0,1
	s = "less than" if a < b else "not less than"
	print(s)

if __name__ == "__main__": main()


# Using strings

def main():
	n = 42
	s = "This is a {} string!" .format(n) 	# Python - V3
	# s = "This is a %s string!" %n 		# Python - V2
	# backslash after initial quotation removes blank line at beginning 
	print(s)

	y = ''' \
	this is a string
	line after line
	of text and more
	text.
	'''
	print(y)

if __name__ == "__main__": main()


# Aggregating values with lists and tuples 

def main():
	x = (1,2,3)
	# Tuples are immutable and thus cannot be appended/changed 
	# x.append(5) 
	# x.insert(2,7)
	for i in x:
		print(i)
	print(type(x),x)

	y = 'string'
	print(type(y),y[2:4])

if __name__ == "__main__": main()


# Creating associative lists with dictionaries 

def main():
	# d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
	# for k in sorted(d.keys()):
	# 	print(k, d[k])

	d = dict(
		one = 1, two = 2, three = 3, four = 4, five = "five"
		)
	d["seven"] = 7
	for k in sorted(d.keys()):
		print(k, d[k])


if __name__ == "__main__": main()

# x == y compares values i.e. test of equality
# x is y compares id

# For loop is used for stepping through iterators
# Virtually all container types in Python are iterators


# Enumerating iterators 

def main():
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line)

    s = "this is a string"
    for i, c in enumerate(s):
    	# print(i,c)
    	if c == "s": print("index {} is an s" .format(i))


if __name__ == "__main__": main()


# Controlling loop flow with break, continue, and else 

def main():
	s = "this is a string"
	# for c in s:
	# 	# if c == "s": break
	# 	print(c)
	i = 0
	while(i < len(s)):
		print(s[i])
		i += 1
	else:
		print("else")

if __name__ == "__main__": main()


# Operating on bitwise values

def b(n): print("{:08b}" .format(n))

b(5)	# print binary value to 8-places

x,y = 0x55, 0xaa
b(x | y)
b(x & y)
b(x ^ y)
b(x ^ 0)
b(x ^ 0xff)
b(x << 4)
b(x >> 4)
b(~x)


# Slices are parts of a container
# Subscripts of container objects are 0-based

list = []
list = [1,2,3,4,5,6,7,8,9,10]

print list[0]
print list[0:5]
	# Ranges ARE NOT inclusive; never include the last item 

list[:] = range(100)
print list[27:42:3]
	# Provides every third element
	# [index where begin: index where end (optional): step (iterator)]

list[27:43:3] = (99,99,99,99,99,99)
	# Assign values with a splice operator 
print list


# Searching with regular expressions 

import re

def main():
    fh = open('raven.txt')
    for line in fh:
    	
    	match = re.search('(Len|Neverm)ore', line)
    	if match:
    		print(match.group())
        
        # if re.search('(Len|Neverm)ore', line):
            # print(line)

if __name__ == "__main__": main()


# Replacing with regular expressions 

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # print(re.sub('(Len|Neverm)ore', '###', line))
        match = re.search('(Len|Neverm)ore', line)
        if match:
        	print(line.replace(match.group(), '###'))

if __name__ == "__main__": main()


# Reusing regular expressions with re.compile

import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
    	if re.search(pattern, line):
    		# print(line)
    		print(pattern.sub('###', line))

if __name__ == "__main__": main()


# Handling exceptions 

def main():
	try:
		fh= open('xlines.txt')
	except IOError as e:
		print("could not open the file:", e)
	# else:
	# 	for line in fh: print(line.strip())

if __name__ == "__main__": main() 


# Raising exceptions -- works only in Python 3??

def main():
    try:
        for line in readfile('xlines.txt'): print(line.strip())
    except IOError as e:
        print("cannot read file:", e)
        
def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError("Filename must end with .txt")

if __name__ == "__main__": main()


# Defining functions 

def main():
    testfunc(42)

# def testfunc(number, another = 43, onemore = 75):	
	# If arguments are defined, must be passed. Alternatively, can assign default values
def testfunc(number, another = None, onemore = 75):	    
	# 'value = None' makes value optional in function
    print('This is a test function', number, another, onemore)
    # pass 	
    	# place holder to make syntax correct

if __name__ == "__main__": main()


# Using lists of arguments

def main():
    testfunc(1,2,3,42,43,45,46)

def testfunc(this, that, other, *args):
    print(this, that, other, args)
    for n in args: print(n)

if __name__ == "__main__": main()


# Using named function arguments 

def main():
    testfunc(5,6,7,8,9,10, one=1, two=2, four=42)
    # required order = named arguments, arbitrary tuple arguments, keyword arguments

def testfunc(this, that, other, *args, **kwargs):
	# kwargs is a dictionary
    # print("This is a test function",
    # 	this, that, other, args,
    # 	kwargs['one'], kwargs['two'], kwargs['four'])
	
	for k in kwargs: print(k, kwargs[k])
	# printed in no particular order

	for n in args: print(n)
	# tuple will be printed in order they were asked 

if __name__ == "__main__": main()


# Returning values from functions

def main():
    print(testfunc())

def testfunc():
    # return "This is a test function"
    # return 42
    return range(25)


if __name__ == "__main__": main()


# Creating a sequence with a generator function

# def main():
#     print("This is the functions.py file.")
#     for i in inclusive_range(0,25,1):
#         print(i)

# def inclusive_range(start, stop, step):
# 	i = start
# 	while i <= stop:
# 		yield i
# 		i += step


def main():
    print("This is the functions.py file.")
    # for i in inclusive_range(25):
    # for i in inclusive_range(5, 25):
    for i in inclusive_range(5,25,3):
    # for i in inclusive_range(5,25,3,42):
    # for i in inclusive_range():
        print(i)

def inclusive_range(*args):
	numargs = len(args)
	if numargs < 1: raise TypeError('requires at least one argument')
	elif numargs == 1:
		stop = args[0]
		start = 0
		step = 1
	elif numargs == 2:
		(start, stop) = args
		step = 1
	elif numargs == 3:
		(start, stop, step) = args 
	else: raise TypeError("inclusive_range expected at most 3 arguments, got {}" .format(numargs))
	i = start
	while i <= stop:
		yield i
		i += step

if __name__ == "__main__": main()


# Understanding classes and objects 

class Duck:
	# Below are suite of class definitions 

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    print(donald)
    # donald is object of class Duck

    donald.quack()
    # look inside the object donald for an attribute called quack
    # Call the methods inside the donald object of class Duck using dot notation

    donald.walk()

if __name__ == "__main__": main()


# Using methods 

class Duck:
    def __init__(self, value):     # Create constructor - most common purpose is to initialize some data
        self._v = value
            # Creates a local variable that is an attribute of the object, not the class
            # Variable can be used in methods 

    def quack(self):
            print('Quaaack!', self._v)

    def walk(self):
            print('Walks like a duck.', self._v)

def main():
    donald = Duck(47)
    frank = Duck(151)

    donald.quack()
    donald.walk()

    frank.quack()
    frank.walk()

if __name__ == "__main__": main()


## Using object data 

class Duck:
    # def __init__(self, color = "white"):
        # self._color = color
        
        ## Good practice to give variables default values unless they are absolutely required
        ## self is a reference to the object 
        ## named with an underscore >> indication that 
            ## it is an attribute used locally 
            ## it will not be used directly - all of the access will be done from methods within the object

        ## use dictionary with keyword arguments to set several arguments to scale
    # def __init__(self, **kwargs):
    #     self._color = kwargs.get('color', 'white')
            ## default color is white

    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # def set_color(self, color):
    #     # self._color = color
    #     self.variables['color'] = color

    # def get_color(self):
    #     # return self._color
    #     return self.variables.get('color', None)
    #         # default color is None

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)



def main():
    
        ## object oriented programming can avoid side effects with the advantage of encapsulation
    # donald = Duck()
    # print(donald.get_color())
    # donald.set_color("blue")
    # print(donald.get_color())

    # donald = Duck()
    # print(donald.get_color())
    # donald = Duck(color='blue')
    # print(donald.get_color())

    donald = Duck()
    print(donald.get_variable('color'))
    donald = Duck(color='blue')
    print(donald.get_variable('color'))
    donald = Duck(feet = 2)
    print(donald.get_variable('feet'))

    donald.set_variable('color', 'blue')
    print(donald.get_variable('color'))

    donald.quack()
    donald.walk()

if __name__ == "__main__": main()


## Understanding inheritance 

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes')

class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        # super().walk()
            ## Built-in function that accesses the parent class i.e. donald will do both actions
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):
        print('I have brown and white fur')
 
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
        ## Walk in duck overrides walk in animal 
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()


## Applying polymorphism to classes 
## Any object of any class that implements the interface that is expected by any function can be used by that function

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
            print('The duck cannot bark')

    def fur(self):
        print('The duck has feathers')

class Dog:
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('The dog cannot quack')


def main():
    donald = Duck()
    # donald.quack()
    # donald.walk()

    fido = Dog()
    # fido.bark()
    # fido.fur()

    for o in (donald, fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_forest(cat):
        ## cat is the variable name
    cat.bark()
    cat.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()


if __name__ == "__main__": main()


## Using generators

## Generate range function that is inclusive
class inclusive_range:
    def __init__(self, *args):
        ## constructor
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}' .format(numargs))

    def __iter__(self):
        ## iterable object 
        i = self.start
        while i <= self.stop:
            yield i
                ## yield function makes it a generator 
                ## yield returns the value and the next time the iterator is called execution picks up right after the yield statement rather than starting at the beginning of the function
            i += self.step


def main():
    # o = range(25)
        ## start [0] and step[1] are default variables of range
    # o = inclusive_range(5,25,7)
    # o = inclusive_range()
    # o = inclusive_range(2,3,4,6)
    # for i in o: print(i)
    for i in inclusive_range(5,25,7): print(i)

if __name__ == "__main__": main()


## Using decorators

## Function in creating accessor methods for variables 
## Can fundamental change the behavior of a function
## Have function methods which are operating a setters and getters >> calling them in simple normal properties syntax

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property
        ## Turns into an acessor for the variable called color 
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']


def main():
    donald = Duck()
    print(donald.color)
    donald.color = 'blue'
    print(donald.color)

if __name__ == "__main__": main()


## String methods 

def main():
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())

if __name__ == "__main__": main()


## tuples created with () and are immutable 
	## prevent accidental changes 
	## functions can be applied as long as it does not modify its contents 
## lists created with [] and are mutable 
## Can assign things to lists but not tuples 


## Operating on character data with bytes and byte arrays 
## Syntax specific to Python V3

def main():
    fin = open('utf8.txt', 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('&#{:04d}' .format(ord(c)), encoding = 'utf_8')
            else: outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print("Done.")


if __name__ == "__main__": main()

## Can operate on character data because characters are bytes and a bytearray is mutable


## Reading and writing text files 

## Buffer mode allows reading files in byte size

def main():
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.')
        buffer = infile.read(buffersize)


if __name__ == "__main__": main()


## Reading and writing binary files 

def main():
    buffersize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.')
        buffer = infile.read(buffersize)
    print()
    print('Done.')


if __name__ == "__main__": main()


## Creating a database with SQLite 3

import sqlite3

def main():
    db = sqlite3.connect('test.db')
        ## create database
    db.row_factory = sqlite3.Row
        ## specify how rows will be returned from the cursor
    db.execute('drop table if exists test')
        ## insert text into database
    db.execute('create table test (t1 test, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)' , ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)' , ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)' , ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)' , ('four', 4))
    db.commit()
    # cursor = db.execute('select * from test order by t1')
        ## step through cursor as iterative object 
        ## ordered by text
    cursor = db.execute('select * from test order by i1')
        ## ordered by integer
    for row in cursor:
        # print(row)
        print(dict(row))
        # print(row['t1'], row['i1'])

if __name__ == "__main__": main()


## CRUD = create, retrieve, update, delete records 

import sqlite3

def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,))
        ## comma creates tuple; parentheses are for grouping
    return cursor.fetchone()

def update(db, row):
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()

def disp_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( t1 text, i1 int )')

    print('Create rows')
    insert(db, dict(t1 = 'one', i1 = 1))
    insert(db, dict(t1 = 'two', i1 = 2))
    insert(db, dict(t1 = 'three', i1 = 3))
    insert(db, dict(t1 = 'four', i1 = 4))
    disp_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    print('Update rows')
    update(db, dict(t1 = 'one', i1 = 101))
    update(db, dict(t1 = 'three', i1 = 103))
    disp_rows(db)

    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()


## Creating a database object
## ERROR: AttributeError: database instance has no attribute '_db'

import sqlite3

class database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')
    
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()
    
    def insert(self, row):
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), 
            (row['t1'], row['i1']))
        self._db.commit()
    
    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where t1 = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())
    
    def update(self, row):
        self._db.execute(
            'update {} set i1 = ? where t1 = ?'.format(self._table),
            (row['i1'], row['t1']))
        self._db.commit()
    
    def delete(self, key):
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'test'

    def close(self):
            self._db.close()
            del self._filename

def main():
    db = database(filename = 'test.db', table = 'test')

    print('Create table test')
    db.sql_do('drop table if exists test')
    db.sql_do('create table test ( t1 text, i1 int )')

    print('Create rows')
    db.insert(dict(t1 = 'one', i1 = 1))
    db.insert(dict(t1 = 'two', i1 = 2))
    db.insert(dict(t1 = 'three', i1 = 3))
    db.insert(dict(t1 = 'four', i1 = 4))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two'))

    print('Update rows')
    db.update(dict(t1 = 'one', i1 = 101))
    db.update(dict(t1 = 'three', i1 = 103))
    for row in db: print(row)

    print('Delete rows')
    db.delete('one')
    db.delete('three')
    for row in db: print(row)

if __name__ == "__main__": main()


## Using standard library modules 

import sys

def main():
    print('Pyhon version {}.{}.{}' .format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    # print(os.urandom(25))

    import random
    print(random.randint(1,1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == "__main__": main()


## Creating a module 

import sys
import time

__version__ = "1.1.0"

class numwords():
    """
        return a number as words,
        e.g., 42 becomes "forty-two"
    """
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' 
        ), 'quarters': (
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range

    def __init__(self, n):
        self.__number = n;

    def numwords(self, num = None):
        "Return the number as words"
        n = self.__number if num is None else num
        s = ''
        if n < 0:           # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:          # single-digit numbers
            s += self._words['ones'][n]  
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += '-' + numwords(m).numwords()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self):
        "Return the number as a number"
        return str(self.__number);

class saytime(numwords):
    """
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    """

    _specials = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'til',
        'past': 'past'
    }

    def __init__(self, h, m):
        self._hour = abs(int(h))
        self._min = abs(int(m))

    def words(self):
        h = self._hour
        m = self._min
        
        if h > 23: return self._oor     # OOR errors
        if m > 59: return self._oor

        sign = self._specials['past']        
        if self._min > 30:
            sign = self._specials['til']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12

        # hword is the hours word)
        if h is 0: hword = self._specials['midnight']
        elif h is 12: hword = self._specials['noon']
        else: hword = self.numwords(h)

        if m is 0:
            if h in (0, 12): return hword   # for noon and midnight
            else: return "{} {}".format(self.numwords(h), self._words['quarters'][m])
        if m % 15 is 0:
            return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword) 
        return "{} {} {}".format(self.numwords(m), sign, hword) 

    def digits(self):
        "return the traditionl time, e.g., 13:42"
        return "{:02}:{:02}".format(self._hour, self._min)

class saytime_t(saytime):   # wrapper for saytime to use time object
    """
        return the time (from a time object) as words
        e.g., fourteen til noon
    """
    def __init__(self, t):
        self._hour = t.tm_hour
        self._min = t.tm_min

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
        else:
            try: print(saytime(*(sys.argv[1].split(':'))).words())
            except TypeError: print("Invalid time ({})".format(sys.argv[1]))
    else:
        print(saytime_t(time.localtime()).words())

def test():
    print("\nnumbers test:")
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30, 
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000 
    )
    for l in list:
        print(l, numwords(l).numwords())

    print("\ntime test:")
    list = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list:
        print(saytime(*l).digits(), saytime(*l).words())

    print("\nlocal time is " + saytime_t(time.localtime()).words())

if __name__ == "__main__": main()