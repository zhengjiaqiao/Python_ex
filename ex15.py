# -- coding:utf-8 --
# 调用sys模组中的参数变量
from sys import argv
# 共两个参数
script,filename = argv

# 打开ex15_sample,并给txt赋值
ddd = open(filename)

#打印
print "Here's your file %r:"% filename
#调用txt的读取功能 并打印出来
print ddd.read()
ddd.closed
