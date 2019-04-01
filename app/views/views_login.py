# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
from app.views.views_common import Commonhandler
from sqlalchemy import and_,func
from app.models.models import User
from app.tools.orm import ORM
import tornado.concurrent

#定义手也视图
class LoginHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html("login.html")

#接收登录页面传递的账号和密码
class ReceLogin(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        account = self.get_argument('zhanghao')
        passwd = self.get_argument('passwd')
        session = ORM.db()
        rows = session.query(User).filter(User.name==account)
        if rows:
            name = [v.name for v in rows]
            passw = [v.passwd for v in rows]
            if account==name[0] and passwd==passw[0]:
                self.redirect('/')
            else:
                self.write("<h1>账号或密码错误</h1>")
        else:
            self.write("<h1>账号或密码错误</h1>")

#接收App登录页面传递的账号和密码
class AppLogin(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        account = self.get_argument('username')
        passwd = self.get_argument('password')
        session = ORM.db()
        rows = session.query(User).filter(User.name==account)
        if rows:
            name = [v.name for v in rows]
            passw = [v.passwd for v in rows]
            if account==name[0] and passwd==passw[0]:
                self.write('ok')
            else:
                self.write("noeq")
