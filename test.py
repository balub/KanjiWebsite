import csv
import sqlite3

import sqlite3

conn = sqlite3.connect('N3_Kanji.db')
# conn.execute('''CREATE TABLE N3_Kanji(
#             id SERIAL PRIMARY KEY,
#             meaning VARCHAR NOT NULL,
#             hiragana VARCHAR NOT NULL,
#             kanji VARCHAR NOT NULL
#              );''')


# conn.execute('''INSERT INTO N3_Kanji (meaning,hiragana,kanji) VALUES ('Lost property','おとしもの','落とし物')''')
# conn.commit()


# f = open("N3_Kanji.csv", encoding="utf8")
# reader = csv.reader(f)
#
# for meaning, hiragana, kanji in reader:
#     print(f"meaning: {meaning}, Hiragana: {hiragana}, Kanji: {kanji}")
#     conn.execute(f"INSERT INTO N3_Kanji (meaning,hiragana,kanji) VALUES (?,?,?)",(meaning,hiragana,kanji))
# conn.commit()

data = conn.execute("SELECT * FROM N3_Kanji")
for dat in data:
    print(dat[1])

