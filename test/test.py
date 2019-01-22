# # move element from a list to another list
# unconfirm_user = ['Alice','Jerry','Bingo']
# confirm_user = []
#
# while unconfirm_user:
#     curr_user = unconfirm_user.pop()
#     confirm_user.append(curr_user)
#
# for user in confirm_user:
#     user = user.title()
#     print('Having been confirm user is %s' % user)
#
#
# # remove an element all same in a  list
# li = ['cat','dog','bird','cat','duck','sheep','dog']
# print('source list: %s' % li)
# while 'cat' in li:
#     li.remove('cat')
#
# print('current list: %s' % li)
#
# # store input result in dictionary
# flag = True
# wflag = True
# responses = {}
# while flag:
#     name = input('What\'s your name?\n')
#     response = input('Which color do you like?\n')
#     responses[name] = response
#
#     while wflag:
#         repeat = input('keep go on ? yes or no \n')
#         if repeat == 'no' or repeat == 'yes':
#             wflag = False
#             if repeat == 'no':
#                 flag = False
#         else:
#             print('please input correctly\n')
#     wflag = True
# print('--survey results are as below--')
# for n,r in responses.items():
#     print('%s likes %s'% (n,r))

# from common.oracle import Oracle
# from config import readconfig
#
# oracle = Oracle(readconfig.db_url)
# oracle.dict_fetchall("select * from xf_testcase where xf_caseid like 'PO01' and xf_tsid like 'TS07'")
# oracle.dict_fetchall("select xf_locationid from xf_testcase where xf_caseid like 'PO01' and xf_tsid like 'TS07'")
#
# dic = {}
# dic.items()

# dic = {"a":1}
# print(dic.get("a"))
filepath = './userconfig.txt'
with open(filepath,'r',encoding='utf-8') as dic:
##    dic.read()
    for item in dic:
        if item.strip() == 'abc':
            print('ok')
        print(item)
