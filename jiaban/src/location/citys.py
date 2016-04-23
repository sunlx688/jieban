# -*- coding:utf-8 -*-
__author__ = 'SUN'

import requests
from bs4 import BeautifulSoup
import re
from jiaban.src.location.models import *


class City():
    def __init__(self, URL):
        self.URL = URL
        self.UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
        self.headers = {'User-Agent': self.UA}
        self.P = re.compile(u'[\\u4e00-\\u9fa5]')  # 匹配汉字的Unicode码

    def get_citys(self):
        continent = 7  # 洲id
        try:
            res = requests.get(self.URL, headers=self.headers)
            soup = BeautifulSoup(res.content, 'html.parser')
            countrys = soup.find_all(attrs={'data-bn-ipg': 'mplace-index-countrylist'})
            for country in countrys:
                country_link = country['href']  # 国家的链接
                country_name = country.text  # 中英文混合的国家名
                country_link = country_link + 'cityall'
                countryNameEng = self.P.split(country_name)[-1]  # 获取国家名中的英文部分
                countryNameZh = country_name.split(countryNameEng)[0]  # 获取国家名中的中文部分
                try:
                    res = requests.get(country_link, headers=self.headers)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    dls = soup.find_all('dl')[1:]  # 除了热门城市的dl标签
                    for dl in dls:
                        citys = dl.find_all('a')
                        for city in citys:
                            city_name = city.text
                            cityNameEng = self.P.split(city_name)[-1]  # 获取国家名中的英文部分
                            cityNameZh = city_name.split(cityNameEng)[0]  # 获取国家名中的中文部分
                            session = DBsession()
                            ID = session.query(Citys).filter(Citys.id).order_by(
                                Citys.id.desc()).first()  # 获取Citys数据库中的最大ID
                            if ID == None or ID == " ":  # 如果Citys数据库中没有数据
                                new_location = Citys(id=1, continent=continent, countryNameEng=countryNameEng,
                                                     countryNameZh=countryNameZh, cityNameEng=cityNameEng,
                                                     cityNameZh=cityNameZh)
                                print('记录第1个城市信息')
                                session.add(new_location)
                            else:
                                new_location = Citys(id=ID.id + 1, continent=continent, countryNameEng=countryNameEng,
                                                     countryNameZh=countryNameZh, cityNameEng=cityNameEng,
                                                     cityNameZh=cityNameZh)
                                print('记录第%d个城市信息' % (ID.id + 1))
                            session.add(new_location)
                            session.commit()
                            session.close()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    url = "http://m.qyer.com/place/antarctica/" #不同的洲页面
    city = City(url)
    print(city.get_citys())
