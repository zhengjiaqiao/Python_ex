# define x
x = "There are %d types of people."% 10
# define binary
binary = "binary"
# define do_not
do_not = "don't"
# define y
y = "Those who know %s and those who %s."%(binary,do_not)
# print x = print "There are 10 types of people."
print x
# print y = print "Those who know binary and those who don't"
print y
# why %s dosen't have ''
print "I said: %r."% x
print "I also said:'%s'."% y
# define hilarious
hilarious = False
# define joke_evaluation
joke_evaluation= "Isn't that joke so funny?!%r"
print joke_evaluation % hilarious
w = "This is the left side of ..."
e = "a string with a right side."

print w+e
