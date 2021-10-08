import MySQLdb


class MyDataBase:
    # 初始化类
    def __init__(self):
        # 打开数据库连接
        self.db = MySQLdb.connect(host="localhost",
                                  user="root",
                                  password="123456",
                                  db="freebuf",
                                  charset='utf8')
        self.cursor = self.db.cursor()
    # 关闭数据库
    def close(self):
        self.db.close()

    # 向freebuf_table中插入一个元素
    def insertElement(self, element_name, element):
        sql = 'insert into freebuf_table({0}) value("{1}")'.format(element_name, element)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print("{0} insert success".format(element))
        except:
            # Rollback in case there is any error
            print('{0} insert error'.format(element))
            self.db.rollback()

    # 获取单个元素信息
    def getElement(self, element):
        res = []
        sql = 'select {0} from freebuf_table'.format(element)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
            for d in data:
                res.append(d[0])
            print("select success")
        except:
            print('select error')
            self.db.rollback()
        return res

    # 通过序号获取单一元素
    def getElementBySerial(self, element, serial):
        sql = 'select {0} from freebuf_table where serial == {1}'.format(element, serial)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
            print("select success")
        except:
            print('select error')
            self.db.rollback()
        return data

    # 获取全部信息，以list形式返回
    def getAllInformation(self):
        res = []
        sql = 'select * from freebuf_table'
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
            for d in data:
                res.append(d[0])
            print("select success")
        except:
            print('select error')
            self.db.rollback()
        return res
