import requests
import cloudscraper
import json
import pprint
import os

if not os.path.exists("./dcard"):
    os.mkdir("./dcard")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=239238602"

ss = requests.Session()
ss.headers = headers

# scraper = cloudscraper.create_scraper(sess=ss)
# res = scraper.get(url, headers=headers)

# print(res.text)

with open('./dcard.json', 'r', encoding='utf-8') as f:
    jsonData = json.loads(f.read())

# for obj in jsonData:
#     print(obj)

# print(jsonData[0].keys())
# pprint.pprint(jsonData[2])


'''
'mediaMeta': [{'createdAt': '2022-06-21T08:47:33.248Z',
                'height': 3994,
                'id': 'fbf50aac-9152-45e0-90eb-537b6954d2d0',
                'normalizedUrl': 'https://i.imgur.com/3lUagwgl.jpg',
                'tags': ['ANNOTATED'],
                'thumbnail': 'https://i.imgur.com/3lUagwgl.jpg',
                'type': 'image/thumbnail',
                'updatedAt': '2022-06-21T08:52:31.118Z',
                'url': 'https://i.imgur.com/3lUagwgl.jpg',
                'width': 3194},
'''
for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = "https://www.dcard.tw/f/photography/p/" + str(articleObj['id'])
    print(title)
    print(articleUrl)
    for idx, imgObj in enumerate(articleObj['mediaMeta']):
        imgUrl = imgObj['url']
        print("\t", imgUrl)
        imgRes = requests.get(imgUrl, headers=headers)
        try:
            with open('./dcard/{}_{}.jpg'.format(title.replace("/", ""), idx), 'wb') as f:
                f.write(imgRes.content)
        except OSError:
            pass
    print("=====")