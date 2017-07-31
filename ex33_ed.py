def function(a,b,c):
    numbers = []
    while a<b:
        print "At the top a is %d"% a
        numbers.append(a)
        print "Numbers:", numbers
        a= a + c
        print "At the bottom a is %d"%a

function(0,6,1)
