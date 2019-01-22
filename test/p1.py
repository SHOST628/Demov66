# making sandwiches
sandwich_orders = ['tuna sandwich','pastrami sandwich','mongo sandwich','pastrami sandwich','cookie sandwich','pastrami sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I\'m making %s'% sandwich)
    finished_sandwiches.append(sandwich)

print('\nAll sandwiches are finished :')
for sandwich in finished_sandwiches:
    print(sandwich)

# sandwiches sold out
order = 0
while 'pastrami sandwich' in finished_sandwiches:
    finished_sandwiches.remove('pastrami sandwich')
    order += 1
    print('Having sold %s pastrami sandwich ' % order)

print('pastrami sandwiches were sold out,left sandwiches list is as below: %s' % finished_sandwiches)



# travel of your dream
responses = {}
flag = True
wflag = True

while flag:
    name = input('What\'s your name? \n')
    place = input('If you can visit a place in the world,where would you go? \n')
    responses[name] = place

    while wflag:
        repeat = input('Keep going? yes or no \n')
        if repeat == 'yes' or repeat == 'no':
            wflag = False
            if repeat == 'no':
                flag = False
        else:
            print('please input correctly!!!')

    wflag = True

print('\n--survey results are as below--')
for n,p in responses.items():
    print('%s likes to visit %s' % (n,p))

