from MyDataBase import MyDataBase


class MyServer:

    def __init__(self):
        self.myDataBase = MyDataBase()
        self.columnList = self.myDataBase.getStructure("freebuf", "freebuf_table")

    def searchPaper(self, paperName):
        resDict = {}
        res = self.myDataBase.selectLike("paper_name", paperName)
        for r in res:
            d = {}
            for i in range(1, len(self.columnList)):
                d[self.columnList[i]] = r[i]
                resDict[i] = d
        return resDict





if __name__ == '__main__':
    m = MyServer()
    print(m.searchPaper("web"))
