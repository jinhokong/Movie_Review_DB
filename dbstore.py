import pymysql
def store(Rno,Ruser,Rstar,Rident,Rreview,Rsite=1,favorite_FNo=None):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='a*70427042',db='moviewatch' ,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,port=8888)
    cur=conn.cursor()
    cur.execute("use moviewatch")
    cur.execute("insert into review(Rno,Ruser,Rstar,Rident,Rreview,Rsite,favorite_FNo) VALUES('%d','%s','%d','%d','%s','%d','%d')" %(Rno,Ruser,Rstar,Rident,Rreview,Rsite,favorite_FNo))
    cur.connection.commit()