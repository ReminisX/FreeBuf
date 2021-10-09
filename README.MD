## FreeBuf爬取项目
该项目爬取FreeBuf上的文章链接，并对每一个文章中的GitHub项目进行追踪爬取，获取其项目名称和星级

### MySelenium.py
模拟浏览器渲染函数，主要通过模拟浏览器渲染完成翻页操作

### getLink.py and getLinks.py
单线程、多线程爬取页面上的GitHub链接

### MainPage.py
主页信息爬取，通过渲染翻页实现爬取二级目录的链接

### MyFlask.py
预设函数，向外暴露服务

### MyDataBase.py
数据库对接函数，其中实现了各类数据库的基本操作

### getGithubInformation.py
根据GitHub地址，调用GitHub的Api，获取信息