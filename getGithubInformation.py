# 更改url为GitHub的api
import json
import requests

from MyDataBase import MyDataBase

# 根据Github项目地址获取api
def getApi(url):
    strs = url.split("/")
    if len(strs) <= 4:
        print("该链接未链接到项目")
    else:
        userName = strs[2]
        projectName = strs[3]
        return "https://api.github.com/repos/{0}/{1}".format(userName, projectName)

# 根据GitHub项目地址生成api
def changeUrl(url):
    strs = url.split("/")
    l = len(strs)
    res = strs[0] + "//" + "api." + strs[2] + "/repos/"
    for i in range(3, l):
        res = res + strs[i] + "/"
    return res


myDataBase = MyDataBase()
dataBaseSize = myDataBase.getSize()

for i in range(1, dataBaseSize + 1):
    print("=" * 50)
    githubUrl = myDataBase.getElementBySerial("github_url", i)
    if githubUrl is None or len(githubUrl) <= 0:
        print("序列{0}无GitHub项目".format(i))
    else:
        githubApi = getApi(githubUrl)
        if githubApi is None or len(githubApi) == 0:
            continue
        r = requests.get(githubApi)
        d = json.loads(r.text)
        if d.get('name') is None or d.get('watchers') is None:
            print("序号{0}无法查询到详细信息,项目地址为{1},项目api为{2}".format(i, githubUrl, githubApi))
            print(d.get('message'))
        else:
            name = d['name']
            star = d['watchers']
            print("序号{0}的GitHub链接为{1},其项目名称为{2},项目star为{3}".format(i, githubUrl, name, star))
            myDataBase.updateElementBySerial("project_name", name, i)
            myDataBase.updateElementBySerial("star", star, i)
