# -- coding:utf-8 --
from sys import argv

script,filename = argv

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm goint to write these to the file."
target.write("%s\n%s\n%s"%(line1,line2,line3))

print "And finally,we close it."
target.close()
