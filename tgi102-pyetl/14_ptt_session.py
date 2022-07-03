import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

url_landing_page = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
url_ask_over_18 = "https://www.ptt.cc/ask/over18"
url_ptt = "https://www.ptt.cc/bbs/Gossiping/index.html"

data = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes"
}

ss = requests.session()

print(ss.cookies)

ss.get(url_landing_page, headers=headers)

print(ss.cookies)

ss.post(url_ask_over_18, headers=headers, data=data)

print(ss.cookies)

res = ss.get(url_ptt, headers=headers)

print(ss.cookies)
print(res.text)
