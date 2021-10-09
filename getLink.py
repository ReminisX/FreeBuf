import re
import time
from concurrent.futures.thread import ThreadPoolExecutor
import numpy as np
import requests
from bs4 import BeautifulSoup
from MyDataBase import MyDataBase
from fake_useragent import UserAgent

# 从url池中获取链接总数
myDataBase = MyDataBase()
# 浏览器伪装头
ua = UserAgent()


def getResponose(url):
    header = {"user-agent": ua.random}
    try:
        response = requests.get(url, headers=header)
    except:
        print("{0}访问失败".format(url))
    return response


# 信息爬取函数
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
            # github链接爬取
            github_link = bs.find_all('a', {'href': re.compile('https://github.com*')})
            # 项目名称爬取
            paperNameObj = bs.find(name='span', attrs={"class": "title-span"})
            # 空值判断
            if paperNameObj is None:
                peperName = ""
            else:
                paperName = paperNameObj.text
            if len(github_link) >= 1:
                github_url = github_link[0]['href']
            else:
                github_url = ""
            # 结果打印
            print("爬取到的github链接为: " + str(github_url))
            print("项目名称是{0}".format(paperName))
            # 数据存储
            myDataBase.updateElementBySerial("github_url", github_url, i)
            myDataBase.updateElementBySerial("paper_name", paperName, i)


dataBaseSize = myDataBase.getSize()
getInformation(1, dataBaseSize+1)
