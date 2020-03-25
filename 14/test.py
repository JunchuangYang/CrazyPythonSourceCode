#__author__ = 'lenovo'
import threading, queue

# 创建一个只有1个元素的队列
bq = queue.Queue(1)
# 创建线程锁
lock = threading.RLock()


def action1(bq):
    for i in range(1, 53, 2):
        # 向队列中放入元素，因为队列只有一个元素，因此放入元素后该线程被阻塞
        bq.put(i)
        print(i, end='')
        print(i + 1, end='')


def action2(bq):
    for i in range(26):
        # 从队列中取出元素，取出元素后，队列为空当前线程被阻塞
        bq.get()
        print(chr(65 + i), end='')


# 创建并启动第一个线程
t1 = threading.Thread(target=action1, args=(bq,))
t1.start()
# 创建并启动第二个线程
t2 = threading.Thread(target=action2, args=(bq,))
t2.start()
