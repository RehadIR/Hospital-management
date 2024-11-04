import pymysql
db=pymysql.connect(user="root",password="",host="localhost",database="hospdb")
def selectone(q):
    cu=db.cursor()
    cu.execute(q)
    d=cu.fetchone()
    return d
def insert(q):
    cu=db.cursor()
    cu.execute(q)
    db.commit()
def selectall(q):
    cu=db.cursor()
    cu.execute(q)
    d=cu.fetchall()
    return d
    