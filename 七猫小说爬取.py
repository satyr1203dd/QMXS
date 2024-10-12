# coding=utf-8
# coding=gbk
# coding=gb2312

import requests
from bs4 import BeautifulSoup

def downloadPage1(url1):
    res1=requests.get(url1)
    soup1 = BeautifulSoup(res1.text, "html.parser")

    title1 = soup1.find('h2', class_="chapter-title").get_text()
    page1 = title1 + '.txt'
    list_conn = soup1.find_all('div', class_='article')
    for e in list_conn:
        with open(page1, 'w+') as f:
            print(f"[+]当前正在下载{page1}")
            f.write(str(e.text))
def downloadPage(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.find('h2', class_="chapter-title").get_text()
    page1 = title + '.txt'
    list_conn = soup.find_all('div', class_='article')
    for e in list_conn:
        with open(page1, 'w+') as f:
            print(f"[+]当前正在下载{page1}")
            f.write(str(e.text))

try:
        pageNum = int(input('[+]请输入你要下载多少章的小说：'))
        if pageNum == 1 :
            url1="https://www.qimao.com/shuku/149774-316193/"
            downloadPage1(url1)
finally:
            url1 = "https://www.qimao.com/shuku/149774-316193/"
            downloadPage1(url1)
            for i in range(317271, 317271 + pageNum - 1):
             url = "https://www.qimao.com/shuku/149774-" + str(i) + '/'
             downloadPage(url)

