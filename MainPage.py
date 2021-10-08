import re
from bs4 import BeautifulSoup

from MyDataBase import MyDataBase
from MySelenium import MySelenium

domain = "https://www.freebuf.com"
url = "https://www.freebuf.com/sectool"
mySelenium = MySelenium()
myDataBase = MyDataBase()
maxPage = mySelenium.getMaxPage(url)

# 首页信息爬取
for page in range(1, maxPage + 1):
    urlList = []
    print("==========正在爬取第{0}页的数据==========".format(page))
    html = mySelenium.getResponse(url, page)
    soup = BeautifulSoup(html, features='html.parser')
    course_links = soup.find_all('a', {'href': re.compile('/sectool/*')})
    for link in course_links:
        urlList.append(link['href'])
    urls = list(dict.fromkeys(urlList).keys())
    print("本次共爬取{0}条数据".format(len(urls)))
    # 循环爬取数据
    for i in range(len(urls)):
        # url拼接
        urls[i] = domain + urls[i]
        # 存入数据库中
        myDataBase.insertElement("paper_url", urls[i])
# 关闭数据库
myDataBase.close()
