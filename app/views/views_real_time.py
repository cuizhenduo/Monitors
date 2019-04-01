# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSConnection
from app.tools.monitor import Monitor
import json
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
        try:
            m = Monitor()
            data = dict()
            if message == "system":
                data = dict(
                    mem = m.mem(),
                    swap = m.swap(),
                    cpu = m.cpu(),
                    disk = m.disk(),
                    net = m.net(),
                    dt = m.dt()
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
