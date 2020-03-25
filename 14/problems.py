#__author__ = 'lenovo'

import threading
from concurrent.futures import ThreadPoolExecutor

'''
https://blog.csdn.net/zhouyong80/article/details/103229301
启动3个线程打印递增的数字，控制线程1打印1,2,3,4,5（每行都打印线程名和一个数字〉，线程2打印6,7,8,9,10 ，
线程3打印11,12,13,14,15； 接下来再由线程1打印16,17,18,19,20……依此类推，直到打印75。
'''

# 新建一个类控制线程锁
class MyThread():
    def __init__(self):
        #当前打印值
        self.number = 0
        #控制应由哪个线程打印
        self.state = 1
        #使用condition来控制线程通信
        self.con = threading.Condition()
    # 打印方法，连续打印5个数字以后就退出当前线程，把执行权限交给下一个线程
    def print(self,thred_num):
        try:
            # 为当前线程加锁
            self.con.acquire()
            # 如果当前线程不是应该执行打印任务的线程，则阻塞当前线程
            if self.state != thred_num:
                self.con.wait()
            # 打印5个连续数值：
            for i in range(5):
                self.number += 1
                print("thread{0},{1}:number{2}".format(threading.current_thread().name,thred_num,self.number))
            # 每打印5个数字后，将thread_num即state值加1，控制由下一个线程来执行打印任务
            self.state = self.state%3 + 1
            # 唤醒所有线程
            self.con.notify_all()

        finally:
            # 释放锁
            self.con.release()

#线程执行体
def action(mt,thread_num):
    # 控制每个线程要执行MyThread对象的my_print()方法5次
    for i in range(5):
        mt.print(thread_num)

def main1():
    #创建MyThread()对象
    mt = MyThread()
    # 创建一个包含三个线程的线程池
    with ThreadPoolExecutor(max_workers=3) as pool:
        # 启动3个线程
        for i in range(3):
            # 使用线程池启动3个线程
            pool.submit(action,mt,i+1)

'''
编写两个线程，其中一个线程打印1~52；另一个线程打印A～Z，打印顺序是12A34B56C … 5152Z。该练习题需要利用多线程通信的知识。
'''
class MyThead2():
    def __init__(self):
        self.number = 1
        self.letter = ord('A')
        self.con = threading.Condition()
        self.state = 'th1'

    def print(self):

        self.con.acquire()

        try:

            if threading.current_thread().name != self.state:
                self.con.wait()

            if self.state == 'th1':
                for i in range(2):
                    print(self.number)
                    self.number+=1
                #print(threading.active_count())
                self.state = 'th2'
            else:
                print(chr(self.letter))
                self.letter=self.letter+1
                self.state = 'th1'
            self.con.notify_all()

        finally:
            self.con.release()

def action2(mt2):
    for i in range(26):
        mt2.print()

def main2():
    mt = MyThead2()
    threading.Thread(target=action2,name='th1',args=(mt,)).start()
    threading.Thread(target=action2,name='th2',args=(mt,)).start()



if __name__=='__main__':
    main1()
    #main2()
