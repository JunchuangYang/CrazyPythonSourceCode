#__author__ = 'lenovo'



def Fib(n):

    if n == 1:
        return [0]
    if n == 2:
        return [1]
    if n == 3:
        return [0,1,1]

    Fib_list = [0,1,1]

    for i in range(4,n+1):
        Fib_list.append(Fib_list[i-1-2]+Fib_list[i-1-1])

    return Fib_list

def fibonacci(n):
    result_lst = [1, 1]
    [result_lst.append(result_lst[-1] + result_lst[-2]) for i in range(2, n)]
    return result_lst

#https://blog.csdn.net/zhouyong80/article/details/102637845


if __name__=='__main__':

    # 自己写
    fib = Fib(int(input("请输入一个正整数：")))
    mi = lambda x:x*x
    fib_mi = [mi(item) for item in fib]

    print (fib)
    print(fib_mi)

    # csdn
    print(fibonacci(10))
    # 计算fibonacci数列的元素的平方值
    result = map(lambda x: x * x, fibonacci(10))
    print([e for e in result], end=' ')
