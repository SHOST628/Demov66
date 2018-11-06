import re


string="新增成功GR1243243单号"
No = ''.join(re.findall("[A-Za-z0-9]",string))
print(No)

s1 = '$12$34'
repl = re.findall("\$(.+?)\$",s1)
print(repl)

s2 = '$34$123$1$'
nn = re.sub('\$(.*?)\$','sub',s2,count=1)
print(nn)