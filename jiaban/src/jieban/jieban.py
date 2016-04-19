'''
Created on 2016年4月19日

@author: sunliangxing
'''
import requests
from bs4 import BeautifulSoup

class Jieban():
    def __init__(self):
        self.URL = 'http://m.qyer.com/bbs/thread-2507375-1.html'
        self.UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
        self.headers = {'User-Agent':self.UA}
    def spi(self):
        res = requests.get(self.URL, headers=self.headers)
        soup = BeautifulSoup(res.content, 'lxml')
        title = soup.find(attrs={'class':'bbsForumsTit bbsDLTit'}).text.strip()
        username = soup.find(attrs={'class':'bbsDTuser'}).find('i').text
        releasetime = soup.find(attrs={'class':'bbsDTuser'}).find('span').text
        location = soup.find(attrs={'class':'dgwDest'}).text.strip()
        startdate = soup.find(attrs={'class':'dgwDate'}).find_all('em')[0].text
        enddate = soup.find(attrs={'class':'dgwDate'}).find_all('em')[1].text
        alldate = soup.find(attrs={'class':'dgwDate'}).find_all('em')[2].text
        contact = soup.find(attrs={'class':'dgwContact'}).text
        info = soup.find(attrs={'class':'dgwDetail'}).text
        return username, releasetime, title, location, startdate, enddate, alldate, contact, info

jieban = Jieban()
print(jieban.spi())
