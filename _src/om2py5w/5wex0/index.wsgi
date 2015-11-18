# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

from bottle import Bottle, route, request, template, run, debug

import sae
import sae.kvdb
import time

app = Bottle()

kv = sae.kvdb.Client()

# set the global diary_num
if not kv.get("diary_num"):
    kv.set("diary_num", 0)

# set the global access_num
if not kv.get("access_num"):
    kv.set("access_num", 0)


def get_all_diaries():
    all_diary_keys = kv.getkeys_by_prefix("note")
    diary_values = [kv.get(key) for key in all_diary_keys]
    sorted_diaries = sorted(diary_values, key = lambda x:x["time"])
    return sorted_diaries

def get_all_tags():
    all_tag_keys = kv.getkeys_by_prefix('tag')
    return all_tag_keys

@app.route('/')
def show_diary():
    sorted_diaries = get_all_diaries()
    access_num = kv.get("access_num")
    kv.set("access_num", access_num+1)
    tags = get_all_tags()
    
    return template("diary.tpl", diaries = sorted_diaries, num=kv.get("diary_num"), access=kv.get("access_num"), tags=tags)

@app.route('/', method='POST')
def write_diary():
    key_num = kv.get("diary_num")
    diary_key ="note" + str(key_num)
    kv.set("diary_num", key_num + 1)

    current_time = time.strftime("%Y-%m-%d %H: %M: %S")
    new_line = request.POST.get('new_line', '')
    tag = request.POST.get('tag_input', '')

    if tag:
        diary_value = {"time": current_time, "content": new_line, "tag": tag}
        if kv.get("tag_"+tag):
            tag_diaries = kv.get("tag_"+tag)
            kv.set("tag"+tag, tag_diaries.append(diary_value))
        else:
            kv.set("tag_"+tag, [diary_value])
    else:
        tag = "未归类"
        diary_value = {"time": current_time, "content": new_line, "tag": tag}

    kv.set(diary_key, diary_value)

    sorted_diaries = get_all_diaries()

    tags = get_all_tags()

    return template("diary.tpl", diaries = sorted_diaries, num=kv.get("diary_num"), access=kv.get("access_num"), tags=tags)

@app.route('/', method='DELETE')
def delete_diary():
    for diary in kv:
        kv.delete(diary)
    kv.disconnect_all()
    return "The world has been destroyed."    

application = sae.create_wsgi_app(app)