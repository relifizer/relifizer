i = ('sdfsdf', 'tttttt', '234', '12313')

import sqlite3
conn = sqlite3.connect('/home/master/mountines.db')
cur = conn.cursor()
cur.execute("select * from dht where region='Алтай'")
print(cur.fetchall())