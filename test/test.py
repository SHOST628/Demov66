import re
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
dic = [{"a":1},{"b":2}]
li = [i.values() for i in dic]
print(li)

a = [1]
b = [2]
print(a+b)

