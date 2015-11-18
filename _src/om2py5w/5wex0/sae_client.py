# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

import requests
from xml import html

help_message = """欢迎来到小小日记系统 SAE 版
    type h/help/? for help
    type q/quit to quit
    type r/sync to show history

    ATTENTION: type clear to empty history!!!
    """

server_address = 'http://hysic1986.sinaapp.com'

def get_diary_num():
