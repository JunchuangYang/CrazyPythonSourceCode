#__author__ = 'lenovo'
# coding: utf-8
'''
自定义序列，包含52张牌
'''
def check_key(key):
    if not isinstance(key,int):
        raise TypeError("索引值必须是整数")
    if key>52 or key<0:
        raise IndexError("索引值必须在0~52之间")

class Poker:
    def __init__(self):
        self.flowers = ('♠', '♥', '♣', '♦')
        self.values = ('2', '3', '4', '5', '6', '7', '8', '9'
                       '10', 'J', 'Q', 'K', 'A')
        self.__changed = {}
        self.__deleted = []

    def __len__(self):
        return 52

    def __getitem__(self, key):
        check_key(key)

        if key in self.__changed:
            return self.__changed[key]

        if key in self.__deleted:
            return None

        flowers = key // 13
        values = key % 13
        return self.flowers[flowers] + self.values[values]

    def __setitem__(self, key, value):
        check_key(key)

        self.__changed[key] = value

    def __delitem__(self, key):
        check_key(key)

        if key not in self.__deleted:
            self.__deleted.append(key)

        if key in self.__changed:
            del self.__changed[key]

if __name__ == '__main__':
    cq = Poker()
    print(len(cq))
    print(cq[2])
    print(cq[1])    # '♠3'
    # 修改cq[1]元素
    cq[1] = '♣2'
    # 打印修改之后的cq[1]
    print(cq[1])    # '♣2'
    # 删除cq[1]
    del cq[1]
    print(cq[1])    # None
    # 再次对cq[1]赋值
    cq[1] = '♦5'
    print(cq[1])    # ♦5
    for pk in cq:
        print(pk)
