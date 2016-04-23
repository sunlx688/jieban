# -*- coding:utf-8 -*-
__author__ = 'SUN'
from sqlalchemy.ext import declarative
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker

Base = declarative.declarative_base()


class Continent(Base):
    __tablename__ = 'continent'

    id = Column(Integer, primary_key=True)
    continentNameEng = Column(String(255))
    continentNameZh = Column(String(255))


class Citys(Base):
    __tablename__ = 'citys'

    id = Column(Integer, primary_key=True)
    continent = Column(Integer, ForeignKey(Continent.id))
    countryNameEng = Column(String(255))
    countryNameZh = Column(String(255))
    cityNameEng = Column(String(255))
    cityNameZh = Column(String(255))


engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/jieban')
DBsession = sessionmaker(bind=engine)
