# -*- coding:utf-8 -*-
import time
import datetime
import random
from app.models.models import Kongqishidu,Kongqiwendu,Turangshidu,Turangwendu,Guangzhao
from app.tools.orm import ORM
def dt():
    now = datetime.datetime.now()
    _date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    _date = now.strftime("%Y-%m-%d")
    _time = now.strftime("%H:%M:%S")
    return _date,_time,_date_time

def save_log():
    #空气温度湿度 土壤温度湿度 光照强度
    _date,_time,_date_time = dt()
    #1创建会话
    session = ORM.db()
    try:
        # 空气温度
        kongqiwendu = Kongqiwendu(
            percent=random.uniform(0,35),
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # 空气湿度
        kongqishidu = Kongqishidu(
            percent=random.uniform(0, 100),
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # 土壤温度
        turangwendu = Turangwendu(
            percent=random.uniform(15, 35),
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # 土壤湿度
        turangshidu = Turangshidu(
            percent=random.uniform(-20, 55),
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # 光照强度
        guangzhao = Guangzhao(
            percent=random.uniform(0, 2000),
            create_date=_date,
            create_time=_time,
            create_dt=_date_time
        )
        # 提交至数据块
        session.add(kongqiwendu)
        session.add(kongqishidu)
        session.add(turangwendu)
        session.add(turangshidu)
        session.add(guangzhao)
    except Exception as e:
        session.rollback()
        print(e)
    else:
        session.commit()
    finally:
        session.close()

if __name__ == "__main__":
    while True:
        _date, _time, _date_time = dt()
        print("开始时间:{}".format(_date_time))
        save_log()
        print("结束时间:{}".format(_date_time))
        time.sleep(5)
