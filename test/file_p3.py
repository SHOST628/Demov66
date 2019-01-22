import json

def get_stored_name(path):
    try:
        with open(path) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    except Exception:
        return None
    else:
        return username

def get_new_name(path):
    username = input('please input new username: ')
    with open(path,'w') as file_object:
        json.dump(username,file_object)
    return username

def greet_user():
    username = get_stored_name('username.json')
    if username:
        while True:
            if_true = input('Is this your name %s? yes or no\n' % username)
            if if_true == 'yes':
                print('welcome back %s' % username)
                break
            elif if_true == 'no':
                username = get_new_name('username.json')
                print('welcome back %s ' % username)
                break
            else:
                print('please input yes or no')
    else:
        username = get_new_name('username.json')
        print('we will remember your name %s' % username)

greet_user()