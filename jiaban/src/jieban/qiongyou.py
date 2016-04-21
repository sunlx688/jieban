# -*- coding:utf-8 -*-
__author__ = 'SUN'
import requests
from bs4 import BeautifulSoup
from jiaban.src.jieban.jieban import Jieban


class QiongYou():
    def __init__(self, URL):
        self.URL = URL
        self.UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'
        self.headers = {'User-Agent': self.UA}

    def qiongYou(self):
        res = requests.get(self.URL, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        linkstrs = soup.find_all(attrs={'class': 'bbsForumsTit'})[1:]
        for linkstr in linkstrs:
            links = 'http://bbs.qyer.com/' + linkstr.find('a')['href']
            yield links


def all_links():
    for pagenum in range(1, 101):
        pagelink = "http://m.qyer.com/bbs/forum-2-0-0-%s.html" % (str(pagenum))
        q = QiongYou(pagelink)
        for link in q.qiongYou():
            yield link


for link in all_links():
    Jieban(link).spi()
