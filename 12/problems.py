#__author__ = 'lenovo'

import fileinput

'''
1. 有两个磁盘文件text1.txt和text2.txt ，各存放一行英文字母，要求把这两个文件中的信息合并（按字母顺序排列）
，然后输出到一个新文件text3.txt 中。
'''
with open('text1.txt','r') as f:
    text1 = f.read()

with open('text2.txt','r') as f:
    text2 = f.read()

text3 = list(text1) + list(text2)

print(type(text3))
text3.sort()
with open('text3.txt','w+') as  f:
    f.write(str(text3))

# 使用fileinput
text5 = []

for line in fileinput.input(files=('text1.txt','text2.txt')):
    text5.append(line)
fileinput.close()

text5.sort()
print(text5)

with open('text3.txt','a+') as  f:
    t = []
    for item in text5:
        t +=str(item)
    t.sort()
    f.write("\n"+str(t))

'''
实现一个程序， 该程序提示用户运行该程序时输入一个路径。该程序会将该路径下（及其子目录下）的所有文件列出来。
'''
from pathlib import Path

'''
判断传入的file对象是否是一个目录，如果是一个目录，则递归列出文件
'''
def list_file(file):
    for item in file.iterdir():
        if Path(item).is_dir():
            list_file(item)
        else:
            print(item)

u_input = input("请输入一个路径: ").strip()
u_dir = Path(u_input)
if not u_dir.exists() or not u_dir.is_dir():
    raise ValueError("输入的路径不存在或不是一个目录")

list_file(u_dir)









