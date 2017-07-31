# -- coding:utf-8 --
from sys import argv

script,user_name,beauty = argv
prompt = 'Your answer:'

print "Hi %r,I'm the %s script."%(user_name,script)
print "I'd like ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of compyter do you have?"
computer = raw_input(prompt)

print "Do you want to fuck %r?"% beauty
computer = raw_input(prompt)

#两个相同的变量 以第二个的值为标准
print """
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.Nice.
""" %(likes,lives,computer)
