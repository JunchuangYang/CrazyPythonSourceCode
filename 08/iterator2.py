#__author__ = 'lenovo'
'''
自定义迭代器，访问前面目录下所有的源文件
'''

import  os

def file_generator():
    for filename in os.listdir(r'.'):
        if filename.endswith('.py'):
            yield filename

if __name__ == '__main__':
    fg = file_generator()
    print(next(fg))    # 返回目录中的第一个文件
    print(next(fg))    # 返回目录中的下一个文件
    for el in fg:
        print(el, end=' ')

