from urllib import request
from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

htmlStr = requests.get(url, headers=headers).text
soup = BeautifulSoup(htmlStr, "html.parser")
# soup = BeautifulSoup(htmlStr, "lxml")
# print(soup)

#### findAll ####
print(soup.findAll('a', {'id': 'logo'}))
print(soup.findAll('a'))
# for t in soup.findAll('a'):
#     print(t)
print(soup.findAll('a', id='logo'))
a_logo_tag_list = soup.findAll('a', id='logo')  # list
print(a_logo_tag_list[0])  # tag object
print(a_logo_tag_list[0].text)  # string object
print("https://www.ptt.cc" + a_logo_tag_list[0]['href'])  # get specific attribute value

#### select ####
a_board_tags = soup.select('a[class="board"]')
print(a_board_tags)
print(a_board_tags[0].select('span'))
print(a_board_tags[0].select('span.board-label'))
print(a_board_tags[0].find('span'))


print(type(soup))
print(type(a_board_tags[0]))

