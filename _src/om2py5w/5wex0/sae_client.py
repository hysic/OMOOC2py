# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

import requests
from lxml import html

help_message = """欢迎来到小小日记系统 SAE 版
    type h/help/? for help
    type q/quit to quit
    type r/sync to show history

    ATTENTION: type clear to empty history!!!
    """

#server_address = 'http://hysic1986.sinaapp.com'
server_address = 'http://localhost:8080'


def get_diary_num():
    pass
def read_diary():
    # get the request data from the server page
    r = requests.get(server_address)
    # parse the page content into a nice tree structure
    tree = html.fromstring(r.content)
    # use XPath to get to the html section you want
    diary_content = tree.xpath('//*[@id="diary_content"]/p/text()')

    return diary_content


def write_diary(diary_note):
    rw = requests.post(server_address, data = {'new_line': diary_note})

    print "%s have been sent to the web server." % diary_note

def delete_all_diaries():
    rd = requests.delete(server_address)

def main():
    while True:
        diary_note = raw_input('>>> ')
        if diary_note in ['h', 'help', '?']:
            print help_message
        elif diary_note in ['q', 'quit']:
            print "Bye ~"
            break
        elif diary_note in ['r', 'sync']:
            for line in read_diary():
                print line
        elif diary_note == "delete":
            delete_all_diaries()
            print "wrong"
        else:
            write_diary(diary_note)

if __name__ == "__main__":
    main()