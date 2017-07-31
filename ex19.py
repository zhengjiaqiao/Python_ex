# -- coding:utf-8 --
# 定义函数及他的参数，打印
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!"%cheese_count
    print "You have %d boxes"%boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
@ 给函数传递参数 参数是变量
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)
# 打印 给函数 cheese_and_crackers传递参数 在函数可以做变量和数字的运算
print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese + 100,
amount_of_crackers + 1000)
