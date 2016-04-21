# -*- coding:utf-8 -*-
__author__ = 'SUN'

from sqlalchemy.ext import declarative
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative.declarative_base()


class Info(Base):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    title=Column(String(255))
    username = Column(String(20))
    releasetime = Column(DateTime(6))
    location = Column(String(255))
    startdate = Column(DateTime(6))
    enddate = Column(DateTime(6))
    days = Column(DateTime(6))
    contact = Column(String(255))
    info = Column(String(255))

engine=create_engine('mysql+mysqlconnector://root:root@localhost:3306/jieban')
DBsession=sessionmaker(bind=engine)