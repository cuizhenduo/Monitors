# -*- coding: utf-8 -*-
import os

#获取当前文件所在目录
root_path = os.path.dirname(__file__)

#配置文件
configs = dict(
    debug = True,
    template_path = os.path.join(root_path,"templates"),
    static_path = os.path.join(root_path,"static")
)