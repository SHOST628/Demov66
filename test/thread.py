import threading
from time import ctime
from time import sleep

# def movie(func,loop):
#     for i in range(loop):
#         print("I was watching movie %s at %s"%(func,ctime()))
#         sleep(5)
#
#
# def music(func,loop):
#     for i in range(loop):
#         print("I was listening to the music %s at %s",(func,ctime()))
#         sleep(2)

def super_player(file_,time):
    for i in range(2):
        print("It's playing %s at %s"%(file_,ctime()))
        sleep(time)

threads = []
list = {"怒放的生命.mp3":2,"钢铁侠3.avi":5}

for f,t in list.items():
    thread = threading.Thread(target=super_player,args=(f,t))
    threads.append(thread)


if __name__ == "__main__":
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print("all is done at %s"%ctime())
