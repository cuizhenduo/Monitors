# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSConnection
import json
from app.models.models import Kongqishidu,Kongqiwendu,Turangshidu,Turangwendu,Guangzhao
from app.tools.orm import ORM
#实时监控类
class RealTimeHandler(SockJSConnection):
    #定义连接池 所有客户端的集合
    waiters = set()

    #1建立连接
    def on_open(self, request):
        try:
            self.waiters.add(self)
        except Exception as e:
            print(e)

    #2发送消息
    def on_message(self, message):
        session = ORM.db()
        try:
            data = dict()
            if message == "system":
                kw = session.query(Kongqiwendu).order_by(Kongqiwendu.create_dt.desc()).first()
                ks = session.query(Kongqishidu).order_by(Kongqishidu.create_dt.desc()).first()
                tw = session.query(Turangwendu).order_by(Turangwendu.create_dt.desc()).first()
                ts = session.query(Turangshidu).order_by(Turangshidu.create_dt.desc()).first()
                gq = session.query(Guangzhao).order_by(Guangzhao.create_dt.desc()).first()
                data = dict(
                    kongqiwendu = str(kw.percent),
                    nt = str(kw.create_dt),
                    kongqishidu = str(ks.percent),
                    turangwendu=str(tw.percent),
                    turangshidu=str(ts.percent),
                    guangzhao=str(gq.percent),
                )
            #把消息推送到虽有连接客户端
            self.broadcast(self.waiters,json.dumps(data))
        except Exception as e:
            print(e)

    #关闭连接
    def on_close(self):
        try:
            self.waiters.remove(self)
        except Exception as e:
            print(e)
