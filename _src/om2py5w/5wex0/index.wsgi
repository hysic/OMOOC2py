from bottle import Bottle, route, request, template, run, debug

import sae
import sae.kvdb
import time

app = Bottle()

kv = sae.kvdb.Client()

if not kv.get("diary_num"):
    kv.set("diary_num", 0)

def get_all_diaries():
    all_diary_keys = kv.getkeys_by_prefix("note")
    diary_values = [kv.get(key) for key in all_diary_keys]
    sorted_diaries = sorted(diary_values, key = lambda x:x["time"])
    #return [diary["time"] + '\t' + diary["content"] +'\ttag:' + diary["tag"] for diary in sorted_diaries]
    return sorted_diaries


@app.route('/')
def show_diary():
    sorted_diaries = get_all_diaries()
    return template("diary_bs.tpl", diaries = sorted_diaries)

@app.route('/', method='POST')
def write_diary():
    key_num = kv.get("diary_num")
    diary_key ="note" + str(key_num)
    kv.set("diary_num", key_num + 1)

    current_time = time.strftime("%Y-%m-%d %H: %M: %S")
    new_line = request.POST.get('new_line', '')
    tag = request.POST.get('tag_input', '')
   
    diary_value = {"time": current_time, "content": new_line, "tag": tag}
    kv.set(diary_key, diary_value)

    sorted_diaries = get_all_diaries()

    return template("diary_bs.tpl", diaries = sorted_diaries)

application = sae.create_wsgi_app(app)