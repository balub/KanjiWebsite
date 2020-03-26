from flask import Flask, render_template
import sqlite3
import random

conn = sqlite3.connect('N3_Kanji.db', check_same_thread=False)
app = Flask(__name__)
data = conn.execute('''SELECT * FROM N3_Kanji''')


def getSize():
    data = conn.execute('''SELECT * FROM N3_Kanji''')
    klist = []
    for dat in data:
        klist.append(dat)

    return len(klist)


data_list = []
for dat in data:
    data_list.append(dat)


@app.route("/", methods=["POST", "GET"])
def index():
    kanji = data_list[random.randrange(0, getSize(), 1)]
    return render_template('index.html', kanji=kanji)
