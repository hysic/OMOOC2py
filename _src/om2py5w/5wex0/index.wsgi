from bottle import Bottle, route, request, template, run, debug

import sae
import sae.kvdb
import time

app = Bottle()

kv = sae.kvdb.Client(debug=True)

test_key = "diary"
if not kv.get(test_key):
    kv.set(test_key, [])

@app.route('/')
def show_diary():
    return template("write_diary.tpl", database = kv)

@app.route('/', method='POST')
def write_diary():
    new_line = request.POST.get('new_line', '')
    current_time = time.strftime("%Y-%m-%d %H: %M: %S")
    diary_content = current_time + '\t' + new_line + '\n'

    diary = kv.get(test_key)
    diary.append(diary_content)

    return template("write_diary.tpl", database = kv)

application = sae.create_wsgi_app(app)