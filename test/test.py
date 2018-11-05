import re


string="新增成功GR1243243单号"
No = ''.join(re.findall("[A-Za-z0-9]",string))
print(No)

class test:
     name="xiaohua"
     def run(self):
             return "HelloWord"

a = getattr(test,"name")
setattr(test,"aa","test")
b = getattr(test,"aa")
print(b)
setattr(test,"aa","test2")
B = getattr(test,"vv","找不到此变量")
print(B)
t = test()
print(t.aa)

