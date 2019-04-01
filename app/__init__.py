# -*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import  tornado.options
from tornado.options import options,define
from app.configs import configs
from app.urls import urls
#定义服务端口
define("port",default=8000,type=int,help="端口")
#1自定义应用
class CustomerApplication(tornado.web.Application):
    #重写__init__
    def __init__(self):
        #指定路由规则
        handlers = urls
        #指定配置信息
        settings = configs
        #调用父类__init__,传入参数
        super(CustomerApplication,self).__init__(handlers=handlers,**settings)

#2自定义服务
def creat_server():
    #允许在命令行启动
    tornado.options.parse_command_line()
    #创建http服务
    http_server = tornado.httpserver.HTTPServer(CustomerApplication())
    #绑定监听端口
    http_server.listen(options.port)
    #启动输入输出事件循环
    tornado.ioloop.IOLoop.instance().start()