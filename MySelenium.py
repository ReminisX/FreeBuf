import time

import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MySelenium:

    def __init__(self):
        # 定义一个对象
        self.chrome_options = webdriver.ChromeOptions()
        # 浏览器无界面显示
        self.chrome_options.add_argument("--headless")
        # 忽略证书
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.chrome_options.add_argument("--ignore-ssl-errors")
        # 生成浏览器实例
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)

    # 获取最大页数
    def getMaxPage(self, url):
        browser = webdriver.Chrome(chrome_options=self.chrome_options)
        browser.get(url)
        maxPage = browser.find_element_by_xpath(
            '//*[@id="components-layout-demo-basic"]/section/main/div/div[2]/div[2]/div[22]/ul/li[8]/a')
        return int(maxPage.text)

    # 通过selenium渲染界面，获取指定页数的数据
    def getResponse(self, url, page):
        self.browser.get(url)
        # 确定输入页数的输入口
        inputBox = self.browser.find_element_by_xpath(
            '//*[@id="components-layout-demo-basic"]/section/main/div/div[2]/div[2]/div[22]/ul/li[10]/div/input')
        inputBox.send_keys(page)
        time.sleep(0.2)
        # 按enter键
        inputBox.send_keys(Keys.ENTER)
        time.sleep(0.2)
        page_source = self.browser.page_source
        return page_source
