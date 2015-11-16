from bottle import Bottle, route, request, template, run, debug

import sae
import time
from os.path import exists

app = Bottle()

filename = 'diary.log'

if not exists(filename):
    with open(filename, 'a'):
        pass

@app.route('/')
def show_diary():
    return template("write_diary.tpl", diary_file=filename)

@app.route('/', method='POST')
def write_diary():
    new_line = request.POST.get('new_line', '')

    if new_line == 'clear':
        with open(filename, 'w') as f:
            pass
    else:
        with open(filename, 'a') as f:
            current_time = time.strftime("%Y-%m-%d %H: %M: %S")
            diary_content = current_time + '\t' + new_line + '\n'
            f.write(diary_content)

    return template("write_diary.tpl", diary_file = filename)

application = sae.create_wsgi_app(app)