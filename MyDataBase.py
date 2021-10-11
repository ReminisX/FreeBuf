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

    def getSize(self):
        sql = 'SELECT count(*) FROM freebuf_table'
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            res = self.cursor.fetchall()[0][0]
            return res
        except:
            self.db.rollback()

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
        except:
            self.db.rollback()
        return res

    # 通过序号获取单一元素
    def getElementBySerial(self, element, serial):
        sql = 'select {0} from freebuf_table where serial={1}'.format(element, serial)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()[0][0]
        except:
            self.db.rollback()
        return data

    # 通过序列号插入元素
    def updateElementBySerial(self, element, value, serial):
        sql = 'update freebuf_table set {0}="{1}" where serial={2}'.format(element, value, serial)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
        except:
            self.db.rollback()
        return data

    # 获取单列全部信息
    def getColumn(self, column):
        res = []
        sql = 'select {0} from freebuf_table'.format(column)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
            for d in data:
                res.append(d[0])
        except:
            self.db.rollback()
        return res

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
        except:
            self.db.rollback()
        return res

    # 获取数据库表结构
    def getStructure(self, dataBase, tableName):
        res = []
        sql = "SELECT column_name FROM information_schema.`COLUMNS` where TABLE_SCHEMA = '{0}' and TABLE_NAME = '{1}'".format(
            dataBase, tableName)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
            for d in data:
                res.append(d[0])
        except:
            self.db.rollback()
        return res

    # 模糊查找信息
    def selectLike(self, element, name):
        res = []
        sql = 'select * from freebuf_table where {0} like "%{1}%"'.format(element, name)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            data = self.cursor.fetchall()
            for d in data:
                res.append(d)
        except:
            self.db.rollback()
        return res
