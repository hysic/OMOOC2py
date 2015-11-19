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

if not kv.get("tags"):
    kv.set("tags", {})


def get_all_diaries():
    all_diary_keys = kv.getkeys_by_prefix("note")
    diary_values = [kv.get(key) for key in all_diary_keys]
    sorted_diaries = sorted(diary_values, key = lambda x:x["time"], reverse=True)
    return sorted_diaries

def get_tagged_diaries(tag):
    tagged_diaries = kv.get("tags")[tag]
    sorted_diaries = sorted(tagged_diaries, key = lambda x:x["time"], reverse=True)

    return sorted_diaries

def get_all_tags():
    tag_list = []
    for tag in kv.get("tags"):
        tag_list.append(tag)
    return tag_list

@app.route('/')
def show_diary():
    sorted_diaries = get_all_diaries()
    access_num = kv.get("access_num")
    kv.set("access_num", access_num+1)
    diary_tags = get_all_tags()

    return template("diary.tpl", tags=diary_tags, diaries = sorted_diaries, num=kv.get("diary_num"), access=kv.get("access_num"))

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
        if tag in kv.get("tags"):
            kv.get("tags")[tag].append(diary_value)
        else:
            kv.get("tags")[tag] = [diary_value]
    else:
        tag = "unsorted"
        diary_value = {"time": current_time, "content": new_line, "tag": tag}
        if tag in kv.get("tags"):
            kv.get("tags")[tag].append(diary_value)
        else:
            kv.get("tags")[tag] = [diary_value]

    kv.set(diary_key, diary_value)

    sorted_diaries = get_all_diaries()

    diary_tags = get_all_tags()

    return template("diary.tpl", tags=diary_tags, diaries = sorted_diaries, num=kv.get("diary_num"), access=kv.get("access_num"))

@app.route('/', method='DELETE')
def delete_diary():
    for key in kv.getkeys_by_prefix('note'):
        kv.delete(key)
    kv.set("diary_num", 0)
    kv.set('access_num', 0)
    kv.set('tags', {})
    return "The world has been destroyed."    

@app.route('/<tag>')
def read_tagged_diaries(tag):
    if tag in kv.get("tags"):
        tagged_diaries = get_tagged_diaries(tag)
        access_num = kv.get("access_num")
        kv.set("access_num", access_num+1)
        tags = get_all_tags()
        return template("diary.tpl", diaries = tagged_diaries, num=kv.get("diary_num"), access=kv.get("access_num"), tags=tags)
    else:
        return "Tag %s not found." % tag

application = sae.create_wsgi_app(app)