identity1 = {}
identity1['first_name'] = 'DLai'
identity1['last_name'] = 'Li'
identity1['age'] = 30
#
# for k,v in identity1.items():
#     print('%s 是 %s' % (k,v))
#
# # like number
# l_numbers = {'Amy':3,'Danny':4,'Jekie':6}
# flag = ''
# for k,v in l_numbers.items():
#     flag = input('Is that true,%s?yes or no\n' %k)
#     if flag == 'yes':
#         print('%s likes %d' % (k,v))

# vocabulary table

identity2 = {'first_name':'Ling','last_name':'Li','age':20}
identity3 = {'first_name':'Ling','last_name':'Li','age':20}
people = [identity1,identity2,identity3]
for i in range(len(people)):
    identity = people[i]
    print('第 %d 个人身份信息：' %(i+1))
    for k,v in identity.items():
        print('%s 是 %s' % (k,v))

# pets
miki = {'type':'dog','master':'Lili'}
doli = {'type':'cat','master':'Toby'}
pets = [miki, doli]

# favorite places
favorite_place = {'Toby':['GZ','BJ','YN'],'Suny':['SZ','BJ','YN']}
popular_place = ['BJ','SH','YN']
for pp in popular_place:
    for k,v in favorite_place.items():
        if pp in v:
            print('%s like %s' % (k,pp))

# cities
tu = (1,23,3)
li = list(tu)
li.copy()