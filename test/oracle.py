import cx_Oracle

from config import readconfig


def dict_fetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


conn = cx_Oracle.connect(readconfig.db_url)
cursor = conn.cursor()
# cursor.execute('select * from xf_case')
# print(cursor.fetchall())

# column = [i[0] for i in cursor.description]
# print(column)

# cursor.execute('select * from xf_case where tcid=:0 and tsid=:tsid',('Login_01','TS01'))
cursor.execute("select * from xf_tcdata order by tcid,tsid")

# all = cursor.fetchall()
#
# print(all)

cursor.execute("select * from xf_tsuite")
all = cursor.fetchall()
print(all)
a = 'sd'
print(type(a))
if type(a) == str:
    print("true")
str1 = all[0][2]
tup = tuple(str1.split(','))
str2 = str(tup)
cursor.execute("select * from xf_tcdata where tcid in %s"%(str2))
all = cursor.fetchall()
print(all)
cursor.close()
conn.close()


