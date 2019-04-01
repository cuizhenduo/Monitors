#创建数据库连接会话
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  #创建会话
class ORM:
    @classmethod
    def db(cls):
        mysql_configs = dict(
            db_host="127.0.0.1",
            db_name="monitor",
            db_port=3306,
            db_user="root",
            db_pwd="292215",
        )
        link = "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8".format(
            **mysql_configs
        )
        engine = create_engine(link, encoding="utf-8", echo=False,
                               pool_size=100,
                               pool_recycle=10,
                               connect_args={"charset":"utf8"})
        #创建会话
        Session = sessionmaker(
            bind=engine,
            autocommit=False,#是否自动提交
            autoflush=True,  #自动刷新权限
            expire_on_commit=False
        )
        return Session()