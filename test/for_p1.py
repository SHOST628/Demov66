students = [
    {"name":"阿土"},
    {"name":"小美"}
]

find_name = input("输入要找的名字：\n")

for stu_dict in students:
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break

else:
    print("找不到该名字 %s" % find_name)