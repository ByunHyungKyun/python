import pymysql


def getName():
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    curs = conn.cursor()
    sql = "select s_name from stock group by s_name"
    curs.execute(sql)
    rows = curs.fetchall()
    
    for i,row in enumerate(rows):
        ret.append(row[0])
        
    conn.close()
    return ret

if __name__=='__main__':
    ret = getName()
    for i,row in enumerate(ret):
        print(i)