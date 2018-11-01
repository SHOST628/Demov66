import re


string="新增成功1243243单号"
No = re.findall("\d+",string)
print(No[0])