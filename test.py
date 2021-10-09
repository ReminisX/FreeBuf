# 设置最大线程数
from concurrent.futures import ThreadPoolExecutor
from MyDataBase import MyDataBase


def printNum(k, j):
    print(k)
    print(j)


POOL_SIZE = 10
pool = ThreadPoolExecutor(max_workers=POOL_SIZE)

z = 0
for i in range(1, POOL_SIZE):
    pool.submit(printNum, z, z+1)
    s = "******线程{0}正在执行******".format(i)
    print("*" * (len(s) + 5))
    print(s)
    print("*" * (len(s) + 5))
