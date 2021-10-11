import json

import numpy as np
from flask import Flask

from MyServer import MyServer

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
myServer = MyServer()

# list转成Json格式数据
def listToJson(lst):
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    return str_json


@app.route("/search/<projectName>", methods=["GET"])
def searchInformationByProjectName(projectName):
    res = myServer.searchPaper(projectName)
    return res


host = "127.0.0.1"
port = 5000
app.debug = True
app.run(host, port)
