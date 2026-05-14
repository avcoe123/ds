import urllib.request
res = urllib.request.urlopen("http://127.0.0.1:5000/add").read()
print(res.decode())
