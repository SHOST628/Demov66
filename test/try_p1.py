while True:
    first_number = input('input first number:')
    if first_number == 'q':
        break
    second_number = input('input second number:')
    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError as e:
        print('you can not divide by zero')

    else:
        print('result is %s' % answer)
