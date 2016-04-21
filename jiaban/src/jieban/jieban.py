import requests
from bs4 import BeautifulSoup
from jiaban.src.jieban.models import *


class Jieban():
    def __init__(self, URL):
        self.URL = URL
        self.UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
        self.headers = {'User-Agent': self.UA}

    def spi(self):
        try:
            res = requests.get(self.URL, headers=self.headers)
            soup = BeautifulSoup(res.content, 'html.parser')
            try:
                title = soup.find(attrs={'class': 'bbsForumsTit bbsDLTit'}).text.strip()
                username = soup.find(attrs={'class': 'bbsDTuser'}).find('i').text
                releasetime = soup.find(attrs={'class': 'bbsDTuser'}).find('span').text
                location = soup.find(attrs={'class': 'dgwDest'}).text.strip()
                startdate = soup.find(attrs={'class': 'dgwDate'}).find_all('em')[0].text
                enddate = soup.find(attrs={'class': 'dgwDate'}).find_all('em')[1].text
                days = soup.find(attrs={'class': 'dgwDate'}).find_all('em')[2].text
                contact = soup.find(attrs={'class': 'dgwContact'}).text
                info = soup.find(attrs={'class': 'dgwDetail'}).text
                if contact.split("：")[1] != None and contact.split("：")[1] != "":
                    session = DBsession()
                    ID = session.query(Info).filter(Info.id).order_by(Info.id.desc()).first()
                    if ID == None or ID == " ":
                        new_info = Info(id=1, title=title, username=username, releasetime=releasetime,
                                        location=location, startdate=startdate, enddate=enddate, days=days,
                                        contact=contact, info=info)
                        print('记录第1条结伴信息')
                    else:
                        new_info = Info(id=ID.id + 1, title=title, username=username, releasetime=releasetime,
                                        location=location, startdate=startdate, enddate=enddate, days=days,
                                        contact=contact, info=info)
                        print('记录第%d条结伴信息' % (ID.id + 1))
                    session.add(new_info)
                    session.commit()
                    session.close()
                else:
                    pass
            except AttributeError:
                pass
        except Exception as e:
            print(e)


if __name__ == "__main__":
    jieban = Jieban('http://bbs.qyer.com/thread-2507625-1.html')
    # jieban = Jieban('http://bbs.qyer.com/thread-2507627-1.html')
    jieban.spi()
