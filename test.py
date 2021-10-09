import json

import requests
url = "https://github.com/boy-hack"
r = requests.get("https://api.github.com/repos/MichaelGrafnetter/DSInternals")
d = json.loads(r.text)

def changeUrl(url):
    strs = url.split("/")
    l = len(strs)
    res = strs[0] + "//" + "api." + strs[2] + "/repos/"
    for i in range(3, l):
        res = res + strs[i] + "/"
    return res

print(changeUrl(url))
print(d.get('name'))
