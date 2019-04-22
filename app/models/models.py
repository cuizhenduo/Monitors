# -*- coding: utf-8 -*-
"""
1导入模型继承父类
2导入数据类型
3导入创建字段的类
4定义模型
"""
from sqlalchemy.ext.declarative import declarative_base #模型继承父类
from sqlalchemy.dialects.mysql import BIGINT,DECIMAL,TIME,DATE,DATETIME,VARCHAR#导入字段
from  sqlalchemy import Column  # 创建字段


Base = declarative_base()  #调用
metadata = Base.metadata

#用户信息
class User(Base):
    __tablename__ = "user"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    name = Column(VARCHAR(20))  #内存使用百分比
    passwd = Column(VARCHAR(20))  #内存总量

#设备信息
class Facility(Base):
    __tablename__ = "faci"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    name = Column(VARCHAR(20))  #名称
    stat = Column(VARCHAR(20))  #状态
    address = Column(VARCHAR(60))  #ip地址，用于控制设备
    kind = Column(VARCHAR(20))  #类别

#自动控制
class AutoFaci(Base):
    __tablename__ = "auto"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    stat = Column(VARCHAR(20))  #状态

#空气温度
class Kongqiwendu(Base):
    __tablename__ = "kongqiwendu"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))  #温度使用百分比
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

#空气湿度
class Kongqishidu(Base):
    __tablename__ = "kongqishidu"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))  #湿度使用百分比
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)


# 土壤温度
class Turangwendu(Base):
    __tablename__ = "turangwendu"  # 指定表名称
    id = Column(BIGINT, primary_key=True)
    percent = Column(DECIMAL(6, 2))  # 温度使用百分比
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)


# 土壤湿度
class Turangshidu(Base):
    __tablename__ = "turangshidu"  # 指定表名称
    id = Column(BIGINT, primary_key=True)
    percent = Column(DECIMAL(6, 2))  # 湿度使用百分比
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

# 光照强度
class Guangzhao(Base):
    __tablename__ = "guangzhao"  # 指定表名称
    id = Column(BIGINT, primary_key=True)
    percent = Column(DECIMAL(6, 2))  # 湿度使用百分比
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

#统计内存
class Mem(Base):
    __tablename__ = "mem"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))  #内存使用百分比
    total = Column(DECIMAL(8,2))  #内存总量
    used = Column(DECIMAL(8,2))   #已使用内存
    free = Column(DECIMAL(8, 2))  # 剩余内存
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

#交换分区统计
class Swap(Base):
    __tablename__ = "swap"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))  #内存使用百分比
    total = Column(DECIMAL(8,2))  #内存总量
    used = Column(DECIMAL(8,2))   #已使用内存
    free = Column(DECIMAL(8, 2))  # 剩余内存
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

#cpu统计
class Cpu(Base):
    __tablename__ = "cpu"  #指定表名称
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))  #内存使用百分比
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

if __name__ == "__main__":
    #导入数据库连接驱动
    import mysql.connector
    #导入创建引擎
    from sqlalchemy import create_engine
    #配置连接信息
    mysql_configs = dict(
        db_host = "127.0.0.1",
        db_name = "monitor",
        db_port = 3306,
        db_user = "root",
        db_pwd = "292215",
    )
    """
    连接格式：mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}
    """
    link = "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
        **mysql_configs
    )
    #创建数据库连接引擎，encoding定义编码，echo是输出日志
    engine = create_engine(link,encoding="utf-8",echo=True)

    #映射
    metadata.create_all(engine)