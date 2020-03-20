#__author__ = 'lenovo'
'''
自定义迭代器，迭代器返回1,1+2,1+2+3
'''
class sums:
    def __init__(self,lens):
        self.current_index = 1
        self.current_value = 0
        self.__len = lens

    def __next__(self):
        if self.__len == 0:
            raise StopIteration

        self.current_value = self.current_index + self.current_value
        self.current_index += 1

        self.__len-=1

        return self.current_value


    def __iter__(self):
        return self

s = sums(10)
print(next(s))

for item in s:
    print(item,end=" ")
