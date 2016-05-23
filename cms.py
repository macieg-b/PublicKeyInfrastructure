import MySQLdb
from setting import hostData, userData, passData, dbData

class post(object):
    def __init__(self, naglowek, data, zawartosc):
        self.data=data
        self.naglowek=naglowek
        self.zawartosc=zawartosc

def getInformationPosts():
    db = MySQLdb.connect(host=hostData, user=userData, passwd=passData, db=dbData)
    cur = db.cursor()
    cur.execute("SELECT `naglowek`, `data`, `zawartosc` FROM `information` ORDER BY `data` DESC")
    results=cur.fetchall()
    if (cur.rowcount==0):
        cur.close()
        db.close()
        return None
    else:
        posty=[]
        for row in results:
            posty.append(post(row[0], row[1].strftime("%Y-%m-%d %H:%M:%S"), row[2]))
        cur.close()
        db.close()
        for a in posty:
            print a
        return posty
