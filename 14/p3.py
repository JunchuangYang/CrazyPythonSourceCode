#__author__ = 'lenovo'
from concurrent.futures import ThreadPoolExecutor
import threading
import time, os
from pathlib import Path
'''
有4个线程1,2,3,4。线程l的功能是输出l，线程2的功能是输出2，依此类推。现在有4个文件A,B,C,D ，初始都为空。
让4个文件最后呈现出如下内容：

A：1 2 3 4 1 2...

B: 2 3 4 1 2 3...

C: 3 4 1 2 3 4...

D: 4 1 2 3 4 1...
————————————————
原文链接：https://blog.csdn.net/zhouyong80/article/details/103229301
'''

# 创建文件写入类
class WriteFile:

    def __init__(self):
        # 当前线程ID
        self.current_thread_num = 1
        # 写入文件总数
        self.write_count = 0

    # 创建函数向文件写入数字
    def write_num(self, value):
        # 生成文件位置
        with open(self.current_file_name() + ".txt", 'a+') as f:
            f.write(value + " ")
            print(
                "ThreadNum={0} is executing. {1} is written into file: {2}.txt \n"
                .format(self.current_thread_num, value,
                        self.current_file_name()))
            self.write_count += 1
            self.current_thread_num = int(value)
            self.next_thread_num()

    # 获取当前写入文件的文件名
    def current_file_name(self):
        '''判断接下来要写入哪个文件'''
        tmp = self.write_count % 4
        name_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        return name_map[tmp]

    # 获取下一个进程的ID
    # 根据顺序1234->2341->3412->4123
    def next_thread_num(self):
        if self.write_count % 4 == 0:
            if self.current_thread_num < 3:
                self.current_thread_num += 2
            else:
                self.current_thread_num = (self.current_thread_num + 2) % 4
        else:
            if self.current_thread_num == 4:
                self.current_thread_num = 1
            else:
                self.current_thread_num += 1


wf = WriteFile()
# 创建Condition对象，用于线程间通信
wf.cond = threading.Condition()
# 如果文件已经存在，先将文件删除
for f in ('A', 'B', 'C', 'D'):
    if Path(f + '.txt').exists():
        os.remove(f + '.txt')


# 创建线程体函数
def action(value):
    try:
        # 向每个文件写入6个数字
        for i in range(6):
            try:
                wf.cond.acquire()
                # 保证要写入的值必须与当前线程的id相同
                while int(value) != wf.current_thread_num:
                    wf.cond.wait()
                wf.write_num(value)
                wf.cond.notify_all()
            finally:
                wf.cond.release()
    except Exception as e:
        print("异常{0}".format(e))


# 创建一个包含4个线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程池启动4个线程
    for i in range(4):
        pool.submit(action, str(i + 1))

#原文链接：https://blog.csdn.net/zhouyong80/article/details/103229301