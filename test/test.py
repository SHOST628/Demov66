import re


string="A1.45，b5，6.45，8.82"
print(re.findall("\d+",string))