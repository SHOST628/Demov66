import re
import time
import time


# string="新增成功GR1243243单号"
# No = ''.join(re.findall("[A-Za-z0-9]",string))
# print(No)
#
# s1 = '$12$34'
# repl = re.findall("\$(.+?)\$",s1)
# print(repl)
#
# s2 = '$34$123$1$'
# nn = re.sub('\$(.*?)\$','sub',s2,count=1)
# print(nn)
#
# rq = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# print(rq)

# dic = [{"a":1,"b":2}]
# li = list(dic[0].values())
# print(li)

# tu = ['a']
# print(tuple(tu))
#
# from common.oracle import Oracle
# from config import readconfig
# oracle = Oracle(readconfig.db_url)
# dic = [{"a":1},{"b":2}]
# li = [i.values() for i in dic]
# print(li)
#
# a = [1]
# b = [2]
# print(a+b)
#
# t = time.strftime('%Y-%m-%d',time.localtime())
# print(t)


li = [1,2,3,4]
li1 = [2,4]
li2 = li.pop(2)
print(li2)

import sys
def a():
    print(sys._getframe().f_code.co_name)

str1 = 'D:\javawork\PyTest\src\main.py'
index = str1.rindex('\\')
str1 = str1[index+1:]
print(str1)