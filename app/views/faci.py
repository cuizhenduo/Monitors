# -*- coding: utf-8 -*-
import tornado.web
from app.views.views_common import Commonhandler
import tornado.gen
from app.models.models import Facility
from app.tools.orm import ORM
import tornado.concurrent
#定义设备视图
class FaciHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        session = ORM.db()
        data = session.query(Facility).all()
        self.html("faci.html",data1=dict(faci=data))



#定义温度设备视图
class Faci_wenHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        session = ORM.db()
        data = session.query(Facility).filter(Facility.kind=='温度').all()
        self.html("faci_wen.html",data1=dict(faci=data))

#定义温度设备视图
class Faci_shiHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        session = ORM.db()
        data = session.query(Facility).filter(Facility.kind=='湿度').all()
        self.html("faci_shi.html",data1=dict(faci=data))

#定义温度设备视图
class Faci_guangHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        session = ORM.db()
        data = session.query(Facility).filter(Facility.kind=='光照').all()
        self.html("faci_gunag.html",data1=dict(faci=data))