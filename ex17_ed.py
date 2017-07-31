# -- coding:utf-8 --
from sys import argv
from os.path import exists

script,from_file,to_file = argv

#这样写不需执行关闭操作，写完这一行后，自动关闭
open(to_file,'w').write(open(from_file).read()).closed()
