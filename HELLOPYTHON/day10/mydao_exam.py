import pymysql

class DaoExam:
    def __init__(self):
       self.conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
    
    def myselect(self):  
        ret = []  
        curs = self.conn.cursor()
 
        sql = "select e_id,kor,eng,math from exam"
        curs.execute(sql)
     
        rows = curs.fetchall()
        for row in rows:
            ret.append({'e_id':row[0],'kor':row[1],'eng':row[2],'math':row[3]})
        return ret
    
    def myinsert(self,e_id,kor,eng,math):  
        curs = self.conn.cursor()
        sql = "INSERT INTO exam (e_id,kor,eng,math) VALUES({},{},{},{})".format(e_id,kor,eng,math)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def myupdate(self,kor,eng,math,e_id):  
        curs = self.conn.cursor()
        sql = "update exam set kor={} ,eng={} ,math={}  where e_id={}".format(kor,eng,math,e_id)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def mydelete(self,e_id):  
        curs = self.conn.cursor()
        sql = "delete from exam where e_id={}".format(e_id)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):    
        self.conn.close()

if __name__ == '__main__':
    de = DaoExam()
    list = de.myselect()
    print(list)
    cnt = de.myinsert("1", "50", "40", "60")
    cnt2 = de.myupdate("100", "100", "100","1")
    cnt3 = de.mydelete("1")
    print(cnt)
    print(cnt2)
    print(cnt3)