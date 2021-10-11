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


dataBaseSize = myDataBase.getSize()
for i in range(1, dataBaseSize + 1):
    print("=" * 50)
    githubUrl = myDataBase.getElementBySerial("github_url", i)
    if githubUrl is None or len(githubUrl) <= 0:
        print("序列{0}无GitHub项目".format(i))
    else:
        bs = BeautifulSoup(getResponose(githubUrl).text, features='html.parser')
        starObj = bs.find_all(name='a', attrs={"class": "social-count js-social-count"})
        nameObj = bs.find_all(name='a', attrs={"data-pjax": "#js-repo-pjax-container"})
        if starObj is None or len(starObj) == 0:
            star = 0
            print("序号{0}star获取失败".format(i))
            continue
        else:
            star = starObj[0].text.strip()
        if nameObj is None or len(nameObj) == 0:
            name = ""
            print("序号{0}name获取失败".format(i))
            continue
        else:
            name = nameObj[0].text
        print("序号{0}的GitHub链接为{1},其项目名称为{2},项目star为{3}".format(i, githubUrl, name, star))
        myDataBase.updateElementBySerial("project_name", name, i)
        myDataBase.updateElementBySerial("star", star, i)
