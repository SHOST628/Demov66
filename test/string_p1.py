# num_str = "1.1"
# num_str = "\u00b2"
#
# print(num_str)
# print(num_str.isdecimal())
# print(num_str.isdigit())
# print(num_str.isnumeric())

# hello_str = "hello world"
#
# print(hello_str.startswith("Hello"))
#
# print(hello_str.endswith("world"))
#
# print(hello_str.find("ll"))
# # print(hello_str.index("a"))
# print(hello_str.find("ab"))
#
# print(hello_str.replace("world","python"))

# poem = ["登观雀楼",
#         "王之涣",
#         "百日依山尽",
#         "黄河如海流",
#         "欲穷千里目",
#         "更上一层楼"
#         ]
# for poem_str in poem:
#     print("|%s|" % poem_str.center(10,"　"))

num_str = "0123456789"
print(num_str[-1::-1])

print("a" in {"a":123})

for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    print("执行结束")