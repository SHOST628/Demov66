# count words
def count_words(file_name):
    try:
        with open(file_name) as file_object:
            text = file_object.read()
    except FileNotFoundError:
        pass
    else:
        text_list = text.split()
        count = len(text_list)
        print(text_list)
        print('%s concludes %s words' % (file_name,count))

count_words('data.txt')


def counter():
    while True:
        first_number = input('please input first number\n')
        if first_number == 'q':
            break
        second_number = input('please input second number\n')
        try:
            first_number = float(first_number)
            second_number = float(second_number)
        except ValueError:
            print('please correctly input num')
        else:
            sum = first_number + second_number
            print('%s add %s is %s' % (first_number,second_number,sum))


# def counter():
#     while True:
#         while True:
#             first_number = input('please input first number\n')
#             try:
#                 if first_number == 'q':
#                     break
#                 first_number = float(first_number)
#                 break
#             except ValueError:
#                 print('please correctly input number')
#         if first_number == 'q':
#             break
#         while True:
#             second_number = input('please input second number\n')
#             try:
#                 second_number = float(second_number)
#                 break
#             except ValueError:
#                 print('please correctly input number')
#         sum = first_number + second_number
#         print('%d add %d is %d' % (first_number,second_number,sum))

def count_word(txt,word):
    try:
        with open(txt) as file_object:
            text = file_object.read()
            text = text.lower()

    except FileNotFoundError:
        print('please check file exist or not')
    else:
        try:
            word = word.lower()
        except AttributeError:
            print('please input string to count')
        else:
            count = text.count(word)
            print('%s concludes %d %s'% (txt,count,word))
count_word('data1.txt','heelf')
