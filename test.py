import requests

r = requests.get("https://www.freebuf.com/sectool/287344.html")
print(r.text)
