from urllib import request

url = "http://3.36.54.90/hello_get"

res = request.urlopen(url=url)

print(res.read().decode('utf8'))