import threading,time
zhenglong=[] #蒸笼
#创建2把锁 一把蒸馒头的锁 由伙夫掌管
# 另一把吃馒头的锁 由吃货 掌管
zheng_lock=threading.Lock()
zheng_Cond=threading.Condition(lock=zheng_lock)
chi_lock=threading.Lock()
chi_Cond=threading.Condition(lock=chi_lock)
class huofu(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.setName(name)
    def run(self):
        while True:
            chi_Cond.acquire()#被谁唤醒
            if len(zhenglong)==0:
                #开始蒸馒头
                for i in range(1,11):
                    zhenglong.append(i)
                    time.sleep(0.1)
                    print('正在蒸第{0}个馒头'.format(i))
                print('馒头蒸完了 唤醒吃货们开始吃馒头..')
                chi_Cond.notify_all()#唤醒了吃货们..
            chi_Cond.release()#唤醒了伙夫  他就释放
            #伙夫 进入休眠
            zheng_Cond.acquire()
            zheng_Cond.wait()
            zheng_Cond.release()
class chihuo(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.setName(name)
    def run(self):
        while True:
            chi_Cond.acquire()#同一时刻只有 一个吃货在获取 吃馒头的资源
            global zhenglong
            if len(zhenglong)==0:
                # 开始呼唤伙夫（只叫一次） 蒸馒头 我和其他吃货一起进入休眠
                zheng_Cond.acquire()#锁定叫醒伙夫的线程
                zheng_Cond.notify()#唤醒
                zheng_Cond.release()#释放
                chi_Cond.wait()
            else:
                mantou=zhenglong.pop()
                print('{0} 吃了第{1}个馒头 剩余{2}个馒头'.format(self.getName(),mantou,len(zhenglong)))
                time.sleep(0.1)
            chi_Cond.release()
W=huofu('伙夫')
youran=chihuo('悠然')
niuniu=chihuo('妞妞')
xiaoming=chihuo('小明')
W.start()
youran.start()
niuniu.start()
xiaoming.start()
#保证主线程不死
input()