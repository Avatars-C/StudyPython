'''
os.getcwd()模块函数

功能：获取当前工作目录，即当前python脚本工作的目录路径【无参】

使用方法：os.getcwd()

格式如：a = os.getcwd()
'''

#-*- coding:utf8 -*-
import os
def test():
    b=os.name
    a=os.getcwd()   #Get the current working path
    print(a)
#输出
#C:\Users\zengdengyuan\Desktop\python\os\test


if __name__=='_test_':
    test()



