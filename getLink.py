import re
from concurrent.futures.thread import ThreadPoolExecutor

import numpy as np
import requests
from bs4 import BeautifulSoup
from MyDataBase import MyDataBase

# 浏览器伪装头
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# 从url池中获取链接总数
myDataBase = MyDataBase()


def getResponose(url):
    header = np.random.choice(user_agent_list)[0]
    try:
        response = requests.get(url, headers=header)
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
