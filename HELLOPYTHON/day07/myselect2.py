import pymysql


def getPrices(s_name):
    re=0
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    curs = conn.cursor()
    sql = "select s_price from stock where s_name='{}' ORDER BY crawl_date".format(s_name)
    curs.execute(sql)
    rows = curs.fetchall()
    
    for i,row in enumerate(rows):
        if row[0]==0:
            ret.append(0)
            return ret
            continue
        if i==0:
            re=row[0]
            ret.append(0)                                                                                                                                         
        else:
            re2=((row[0]-re)/re)*100
            re3=0+re2
            ret.append(re3)
    conn.close()
    return ret

if __name__=='__main__':
    ret = getPrices("LG전자")
    print(ret)