# -- coding:utf-8 --
# 逗号的作用是不用换行
print "How old are you ?",
age = raw_input()
print "How tall are you?",
height= raw_input()
print "How much do you weight?",
weight = raw_input()
# input 会根据你的输入变换相应的类型，如果输入字符或字符串必须用""或者''包起来
# raw_input 不管你说的是什么都会转变为字符型。
print "SO,you're %r old,%r tall and %r heavy."%(age,height,weight)
