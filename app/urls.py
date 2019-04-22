# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSRouter
from app.views.views_real_time import RealTimeHandler as time_handler
from app.views.views_index import IndexHandler as index
from app.views.views_log import LogHandler as log
from app.views.views_login import LoginHandler as login,ReceLogin as RL,AppLogin as al
from app.views.faci import FaciHandler as fh,Faci_wenHandler as fwh,Faci_shiHandler as fsh,Faci_guangHandler as fgh
from app.views.views_android_jishi import Android_IndexHandler as ai
from app.views.views_android_log import LogHandler as alog
from app.views.views_ajax import AjaxHandler as ah,AjaxHandlerClose as ahc
#配置视图路由映射规则
urls = [
    (r"/",index),
    (r"/log/",log),
    (r"/login/",login),
    (r"/recelogin/",RL),
    (r"/al/",al),
    (r"/fh/",fh),
    (r"/fwh/",fwh),
    (r"/fsh/",fsh),
    (r"/fgh/",fgh),
    (r"/ai/",ai),
    (r"/alog/",alog),
    (r"/ah/",ah),
    (r"/ahc/",ahc),
]+SockJSRouter(time_handler,"/real/time").urls
