import pymysql


def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    curs = conn.cursor()
     
    sql = "select s_price from stock where s_name='{}'".format(s_name)
    curs.execute(sql)
     
    rows = curs.fetchall()
    for i,row in enumerate(rows):
        ret.append(row[0])
        
    conn.close()
    return ret

if __name__=='__main__':
    ret = getPrices("삼성전자")
    print(ret)