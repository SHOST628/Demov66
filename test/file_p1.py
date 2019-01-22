# all read
file_name = 'data.txt'
with open('data.txt') as file_object:
    text = file_object.read()
    print(text.rstrip())


# read by line
with open('data.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

pi = ''
for line in lines:
    pi += line.rstrip()
print(pi)

# birthday = input('please input your birthday\n')
# if birthday in pi:
#     print('your birthday no concludes in pi')
# else:
#     print('your birthday no not in pi')

# 'r': read   'w':write  'a':attach   'r+':read and write

new_file = 'data1.txt'
with open(new_file,'r+') as file_object:
    # it will not autoly add \n
    file_object.write('Hello!\n')
    file_object.write('Hello World!\n')

with open(new_file,'a') as file_object:
    file_object.write('Jee')


flag = True
wflag = True
while flag:
    file_name = 'guest_book.txt'
    name = input('What\'s your name?\n')
    print('Welcome to be here,%s' % name.title())
    with open(file_name,'a') as file_object:
        file_object.write(name+'\n')
    while wflag:
        repeat = input('Keep going? yes or no\n')
        if repeat == 'yes' or repeat == 'no':
            wflag = False
            if repeat == 'no':
                flag = False
        else:
            print('please input correctly')
    wflag = True

with open(file_name) as file_object:
    text = file_object.read()
    print(text)

