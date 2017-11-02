# Learning Python - Joe Marini _ Lynda.com

# Using Python2.7 as default in lesson
# Confirm installation
python --version

# Run python interpreter 
# python
# >>> exit()

# Uses indentation level of the lines of code to indicate where the code belongs; does not have notion of scope delimiters by “ { } “


## Example file for HelloWorld

print "Hello World"

def main():
	print "Hello World!"

if __name__ == "__main__":
	main()
# "main" function will be called if executed as a program  (vs. library)

print "me too"


## Example file for variables 

# Declare a variable and initialize it
f = 0;
print f

# Re-declare a variable 
f = "abc"
print f

# ERROR: different types cannot be combined
# print "string type" + 123
print "string type" + str(123)

# Global vs. local variables in function 
def someFunction():
	global f 	# presence/absence indicates if value is global/local, respectively
	f = "def"
	print f

someFunction()
print f
# undefine variable
del f


## Example file for working with functions

# Define a function
def func1():
	print "I am a function"

func1()
print func1()
	# print "none" [DEFAULT] because no return function is indicated 
print func1

# function that takes arguments
def func2(arg1, arg2):
	print arg1, " ", arg2

func2(10,20)
print func2(10,20)

# function that returns a value
def cube(x):
	return x*x*x

print cube(3)

# function with default value for an argument
def power(num, x=1):
	result = 1;
	for i in range(x):
		result = result * num
	return result

print power(2)
print power(2,3)
# reverse order of arguments with appropriate variables indicated 
print power(x=3, num=2)

# function with variable number of arguments
	# Asterik indicates that can pass through a variable number of arguments 
def multi_add(*args):
	result = 0;			# local variable result 
	for x in args:
		result = result + x
	return result

print multi_add(4,5,10,4)


## Example file for working with conditional statements 

def main():
	x,y = 10,1000

	# if (x < y): 
	# 	st = "x is less than y"
	# elif (x == y):
	# 	st = "x is the same as y"
	# else:
	# 	st = "x is greater than y"
	# print st

	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
	print st

if __name__ == "__main__":
	main()


## Example file for working with loops

def main():
	x = 0
	# define a while loop
	while (x < 5):
		print x
		x = x + 1

	# define a for loop
	for x in range (5,10): 
		print x

	# use a for loop over a collection
	days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	for d in days:
		print d

	#use the break (i.e. terminates loop) and continue (i.e. go back to start of loop) statements 
	for x in range(5,10):
		#if (x == 7): break
		if (x % 2 == 0): continue
		print x


	# using the enumerate() function to get index
	days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	for i, d in enumerate (days):
		print i, d 

if __name__ == "__main__":
	main()


## Example file for working with classes 

class myClass():
	def method1(self):
		print "myClass method1"

	def method2(self, someString):
		print "myClass method2: " + someString

class anotherClass(myClass):
	def method2(self):
		print "anotherClass method2"

def main():
	# exercise the class methods
	c = myClass()
	c.method1()
	c.method2("This is a string")
	c2 = anotherClass()
	c2.method1()
	c2.method2()

if __name__ == "__main__":
	main()


# Example file for working with date information

from datetime import date
from datetime import time
from datetime import datetime

def main():
	## Date onjects
	today = date.today()
	print "Today's date is ", today

	# print out the date's individual components
	print "Date Components: ", today.day, today.month, today.year

	# retrieve today's weekday (0=Monday, 6=Sunday)
	print "Today's Weekday #: ", today.weekday()

	# Datetime objects
	# Get today's date from the datetime class
	today = datetime.now()
	print "The current date and time is ", today

	# Get the current time
	t = datetime.time(datetime.now())
	print "The current time is ", t

	# Weekday returns 0 (monday) through 6 (sunday)
	wd = date.weekday(today)
	# Days start at 0 for Monday
	days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	print "Today is day number %d " % wd
	print "Which is a " + days[wd]

if __name__ == "__main__":
	main();


## Example file for formatting time and date output

from datetime import datetime

def main():
	# Times and dates can be formatted using a set of predefined string
	# controlcodes

	now = datetime.now() # get the current date and time

	# Date formatting

	print now.strftime("%Y") 
		# full year with century
	print now.strftime("%A, %d, %B, %y") 
		# abbreviated day, num, full month, abbreviated year

	print now.strftime("%c")
		# %c - locale's date and time
	print now.strftime("%x")
		# %x - locale's date
	print now.strftime("%X")
		# %X - locale's time

	# Time formatting

	# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
	print now.strftime("%I:%M:%S %p")
		# 12-Hour:Minute:Second:AM
	print now.strftime("%H:%M")
		# 24-Hour:Minute

if __name__ == "__main__":
	main();


## Example file for working with timedelta objects 

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print timedelta(days=365, hours=5, minutes=1)


# print today's date
print "today is:" + str(datetime.now())

# print today's date one year from now
print "one year from now it will be:" + str(datetime.now() + timedelta(days=365))

# create a timedelta that uses more than one argument
print "in two weeks and 3 days it will be:" + str(datetime.now() + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print "one week ago it was " + s

# How many days until April Fool's Day?

today = date.today() # get today's date
afd = date(today.year, 4, 1) # get April Fool's for the same year
#use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
	print "April Fool's day already went by %d days ago" %((today-afd).days)
	afd = afd.replace(year=today.year + 1) # if so, get the daye for next year

# Now calculate the amount of time until April Fool's Day
time_to_afd = abs(afd - today)
print time_to_afd.days, "days until next April Fool's Day!"


## Example file for working with calendars

import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2013, 1, 0, 0)
print str

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2013, 1)
print str

# loop over the days of a month
# zeros mean that the days of the week is in an overlapping month
for i in c.itermonthdays(2013, 8):
	print i

# The calendar module provides useful utilities for the given locale, 
# such as the names of days and months in both full and abreviated forms
for name in calendar.month_name:
	print name

for day in calendar.day_name:
	print day

# Calculate days based on a rule: For example, consider a team meeting on the first Friday of every month.
# To figure out what days would be for each month, we can use this script - 
for m in range(1,13):
	# return an array of weeks that represents the month
	cal = calendar.monthcalendar(2013, m)
	# the first Friday has to be within the first two weeks
	weekone = cal[0]
	weektwo = cal[1]

	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	else:
		# if the first Friday isn't in the first week, it must be in the second
		meetday = weektwo[calendar.FRIDAY]

	print "%10s %2d" % (calendar.month_name[m], meetday)


## Read and write files using the built-in Python file methods

def main():
	# # Open a file for writing (w) and create it if it doesn't exist (+)
	f = open("textfile.txt", "w+")
	# # Open the file for appending text to the end
	# f = open("textfile.txt", "a+")

	# # Write some lines of data to the file
	# for i in range(10):
	# 	f.write("This is line %d\r\n" % (i+1))

	# # Close the file when done
	# f.close()

	# Open the file back up and read the contents
	f = open("textfile.txt", "r")
	if f.mode == 'r': #check to make sure the file was opened
	# use the read() function to read the entire file
		# contents = f.read()
		# print contents
	# or, readlines reads the individual lines into a list 
		fl = f.readlines()
		for x in fl:	
			print x

if __name__ == "__main__":
	main()


## Example file for working with os.path module 

import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
	# make a duplicate of an existing file
	if path.exists("textfile.txt"):
		# get the path to the file in the current directory
		src = path.realpath("textfile.txt");

		# separate the path part from the filename
		head, tail = path.split(src)
		print "path: " + head
		print "file: " + tail

	# make a backup copy by appending "bak" to the name
	dst = src + ".bak"
	# use the shell to make a copy of the file
	shutil.copy(src,dst)
	# copy over the permissions, modification times, and other info
	shutil.copystat(src, dst)

	# rename the original file
	os.rename("textfile.txt", "newfile.txt")

	# put things into a ZIP archive
	# root_dir,tail = path.split(src)
	# shutil.make_archive("archive", "zip", root_dir)

	# More fine-grained control over ZIP files
	with ZipFile("testzip.zip", "w") as newzip:
		newzip.write("newfile.txt")
		newzip.write("textfile.txt.bak")

if __name__ == "__main__":
	main()


## Example file for retrieving data from the internet

import urllib2

def main():
	# open a connection to a URL 
	webUrl = urllib2.urlopen("http://joemarini.com")

	# get the result code and print it
	print "result code: " + str(webUrl.getcode())

	# read the data from the URL and print it
	data = webUrl.read()
	print data

if __name__ == "__main__":
	main()


## Example file for parsing and processing JSON

import urllib2
import json

def printResults(data):
	# use the json module to load the string data into a directory
	theJSON = json.loads(data)
	# access the contents of the JSON like any other Python object
	if "title" in theJSON["metadata"]:
		print theJSON["metadata"]["title"]

	# output the number of events, plus the magnitude and each event name
	count = theJSON["metadata"]["count"];
	print str(count) + " events recorded"

	# for each event, print the place where it occurred
	for i in theJSON["features"]:
		print i["properties"]["place"]

	# print the events that only have a magnitude greater than 4
	for i in theJSON["features"]:
		if i["properties"]["mag"] >= 4.0:
			print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

	# print only events where at least 1 person reported feeling something
	print "Events that were felt:"
	for i in theJSON["features"]:
		feltReports = i["properties"]["felt"]
		if (feltReports != None) & (feltReports > 0):
			print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"


def main():
	# define a variable to hold the source URL
	# use the free data from the USGS
	# feed lists all earthquakes for the last day larger than Mag 2.5
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	# Open the URL and read the data
	webUrl = urllib2.urlopen(urlData)
	print webUrl.getcode()
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		# print out our customized results
		printResults(data)
	else:
		print "Received an error from server, cannot retrieve results " + str(webUrl.getcode)

if __name__ == "__main__":
	main()


## Example file for parsing and processing HTML

# import the HTMLparser module
from HTMLParser import HTMLParser

metacount = 0;

# create a subclass and override the handler methods
class myHTMLParser(HTMLParser):
	# function to handle an opening tag in the doc
	# this will be called when the closing ">" of the tag is reached 
	def handle_starttag(self, tag, attrs):
		global metacount
		print "Encountered a start tag:", tag
		if tag == "meta":
			metacount += 1
		pos = self.getpos() # returns a tuple indication line and character
		print "At line: ", pos[0], " position ", pos[1]
		if attrs.__len__ > 0:
			print "\tAttributes:"
			for a in attrs:
				print "\t", a[0], "=", a[1]

	# function to handle the ending tag
	def handle_endtag(self, tag):
		print "Encountered an end tag:", tag
		pos = self.getpos()
		print "At line: ", pos[0], " position ", pos[1]

	# function to handle character and text data (tag contents)
	def handle_data(self, data):
		print "Encountered some data:", data
		pos = self.getpos()
		print "At line: ", pos[0], " position ", pos[1]

	# function to handle the processing of HTML comments 
	def handle_comment(self, data):
		print "Encountered comment:", data
		pos = self.getpos()
		print "At line: ", pos[0], " position ", pos[1]

def main():
 	# instantiate the parser and feed it some HTML
	parser = myHTMLParser()

 	# open the sample HTML file and read it
	f = open("samplehtml.html")
 	if f.mode == "r":
 		contents = f.read() # read the entire file
 		parser.feed(contents)

 	print "%d meta tags encountered" % metacount

if __name__ == "__main__":
 	main();


## Example file for parsing and processing XML

import xml.dom.minidom

def main():
	# use the parse() function to load and parse an XML file
	doc = xml.dom.minidom.parse("samplexml.xml");

	# print out the doc node and the name of the first child tag
	print doc.nodeName
	print doc.firstChild.tagName

	# get a list of XML tags from the document and print each one
	skills = doc.getElementsByTagName("skill")
	print "%d skills:" % skills.length
	for skill in skills:
		print skill.getAttribute("name")

	# create a new XML tag and add it into the document 
	newSkill = doc.createElement("skill")
	newSkill.setAttribute("name", "jQuery")
	doc.firstChild.appendChild(newSkill)
	print " "
	
	skills = doc.getElementsByTagName("skill")
	print "%d skills:" % skills.length
	for skill in skills:
		print skill.getAttribute("name")

if __name__ == "__main__":
	main();
