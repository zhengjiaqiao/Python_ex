# -- coding:utf-8 -- 可以输入汉字
# 注释
print “” 打印字符串
+ 两个数相加
/ 两个数相除
* 两个数相乘
% 两个数相除取余数
< 小于
> 大于
>= 大于等于
<= 小于等于
= 为变量赋值
%s 格式化字符 输入字符串 不带引号
%d 格式化字符 输入数字
%r 格式化字符 原样输入 输入字符串时带引号
False bool 类型 错误 可以给变量赋值
pring "string" * num 打印num次
print "string", 末尾加逗号不换行，有空格
print "string"+"string" 连续打印两个字符串，中间没空格 算一个字符串
\n 转义字符 newline 换行
"""string""" 输入多行文字自动换行
\t 转义字符 tab 缩进
\\ 转义字符 打印出\
raw_input 不管你输入什么都会转变为字符型
input 会根据输入变换类型 输入字符串必须带引号
from sys import argv 调用sys模组中的变量参数命令
argv argument variable 整个变量包含了传递给python的参数
unpack 解包 将所有参数赋予变量名
txt = open（file）以只读模式打开文件，可赋值给变量txt
txt.read() 读取文件全部内容
txt.closed 关闭文件
txt = open(file,"w")以写的模式打开文件，并赋值给变量txt
txt.truncate() 清空文件内容
txt.write("string")写入字符串
len()测量字符串、文件的长度
from os.path import exists 调用os.path中的exists命令
exists()将文件名字符串作为参数，如果存在返回True，不存在返回False
open（file."w").write(open(file).read())可以试用无限嵌套的模式，用这种方法文件自动关闭
def 定义函数
*args 含量的参数 类似argv
函数可以有多个参数，也可以没有参数
函数的参数可以做各种运算 数与变量之间
txt.seek(0)指针定位到文件开头
txt.read(num)读取某一行 指针定位到\n处
num+=1 每运行一次 num自动+1
return a+b 返回a+b的值
return a-b 返回a-b的值
return a*b 返回a*b的值
return a/b 返回a/b的值
python -m pydoc input  帮助说明
