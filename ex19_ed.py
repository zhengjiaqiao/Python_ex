from sys import argv
script,input_file=argv

def print_all(argument1,argument2):
    print "I have three point to say:"
    print "%r.I love you"%argument1
    print "%r.I want to fuck you"%argument1
    print "%r.I am gonner show you a leeter"%argument1
    print "%r."%argument1,argument2.read()

current_file=open(input_file)
num = 1
print "first way:"
print_all(num,current_file)

print "second way:"
print_all(2,current_file)

print "third way:"
print_all(num+2,current_file)

print "fouth way:"
print_all("dfdfd",current_file)

print "fifth way:"
print_all(print_all(2,current_file),current_file)
