from flask import Flask
import json
import numpy as np
from MyDataBase import MyDataBase

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
myDataBase = MyDataBase()


# list转成Json格式数据
def listToJson(lst):
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    return str_json


@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/AllUrls", methods=["GET"])
def getAllUrls():
    res = myDataBase.getAllUrl()
    return listToJson(res)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5000
    app.debug = True
    app.run(host, port)
