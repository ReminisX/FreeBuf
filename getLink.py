import re
from concurrent.futures.thread import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from MyDataBase import MyDataBase

# 从url池中获取链接总数
myDataBase = MyDataBase()


def getResponose(url):
    try:
        response = requests.get(url)
    except:
        print("url访问失败")
    return response


# 多线程任务函数，爬取序号从start到end的网页信息
def getInformation(start, end):
    # 循环从url池中获取数据，并爬取相关信息
    for i in range(start, end):
        print("=" * 50)
        print("正在爬取序号{0}的数据...".format(i))
        url = myDataBase.getElementBySerial("paper_url", i)
        print(url)
        response = getResponose(url)
        if response is None:
            print("序号{0}未爬取到数据".format(i))
        else:
            bs = BeautifulSoup(response.text, features='html.parser')
            github_link = bs.find_all('a', {'href': re.compile('https://github.com*')})
            if len(github_link) >= 1:
                github_url = github_link[0]['href']
            else:
                github_url = ""
            print("爬取到的github链接为: " + str(github_url))
            myDataBase.updateElementBySerial("github_url", github_url, i)


# 设置最大线程数
POOL_SIZE = 10
pool = ThreadPoolExecutor(max_workers=POOL_SIZE)
# 根据线程数切分任务
dataBaseSize = myDataBase.getSize()
k = int(dataBaseSize / POOL_SIZE)
start = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
for i in range(1, POOL_SIZE):
    pool.submit(getInformation, start, start+k)
    s = "******线程{0}正在执行[{1}, {2}]任务段******".format(i, start, start+k)
    print("*" * (len(s) + 5))
    print(s)
    print("*" * (len(s) + 5))
    start += k
pool.submit(start, dataBaseSize+1)
fs = "******线程{0}正在执行[{1}, {2}]任务段******".format(POOL_SIZE, start, dataBaseSize)
print("*" * (len(fs) + 5))
print(s)
print("*" * (len(fs) + 5))
