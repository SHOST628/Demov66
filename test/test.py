import re
#
#
# string="新增成功GR1243243单号"
# No = ''.join(re.findall("[A-Za-z0-9]",string))
# print(No)

s1 = '$$12$$34'
repl = re.sub("[\$\$]",'',s1)
print(repl)