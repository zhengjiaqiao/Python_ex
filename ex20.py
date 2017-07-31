# --coding:utf-8--
#调用sys中的argv模组
from sys import argv
#参数解包
script,input_file = argv
#定义函数print_all 为读取全部并打印
def print_all(f):
    print f.read()
#定义函数rewind(f) 为定位到开头
def rewind(f):
    f.seek(0)
#定义函数print_a_line 为打印变量及文件的一整行
def print_a_line(line_count,f):
    print line_count,f.readline()
#将变量current_file赋值为以只读模式打开文件input_file
current_file = open(input_file)
#打印字符串
print "Firse let's print the whole file:\n"
# 调用函数print_all 参数为变量current_file
print_all(current_file)
#打印字符串
print "Now let's rewind,kind of like a tape."
#调用函数rewind 参数为变量current_file 回到文件开头
rewind(current_file)
#打印字符串
print "Let's print three lines:"
#将变量current_line赋值为1
current_line = 1
#调用函数print_a_line 参数为current_line，cunrrent_file 打印行数，以及第一行
print_a_line(current_line,current_file)
# 将变量current_line赋值为其本身+1
current_line += 1
#调用函数print_a_line 参数为current_line current_file  打印行数，以及第二行
print_a_line(current_line,current_file)
#调用函数print_a_line 参数为current_line current_file  打印行数，以及第三行

print_a_line(current_line,current_file)
