import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root',
                       passwd='root', db='mysql')
cur = conn.cursor()
cur.execute("USE caoliu")
# cur.execute(
#    "INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", ('夺朋友', '女朋友'))
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()

cur = conn.cursor()
cur.execute("USE zhongwen")
cur.execute(
    "INSERT INTO pages (title, content) VALUES ("夺朋友","女朋友")")
cur.execute("SELECT * FROM pages")
print(cur.fetchone())
cur.close()
conn.close()
