import re

str1 = "//*[@id='XF_COSTCENTER-%s']"
str2 = (re.findall("\[(.+?)\]",str1))[0]

str3 = str2.replace("=",",")
str4 = "contains(" + str3 + ")"
print(re.sub("\[(.+?)\]",str4,str1,count=1))
