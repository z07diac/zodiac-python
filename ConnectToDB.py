import cx_Oracle

conn=cx_Oracle.connect(user='xx', password='test01', dsn='host:port/scheme')

cursor = conn.cursor()
x=cursor.execute("SQL")
print (x.fetchone())

cursor.close()
conn.close()


