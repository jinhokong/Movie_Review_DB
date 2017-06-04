import pymysql
def store(Rno,Ruser,Rstar,Rreview,Review_site_table_Rsite,movie_MNo,user_CNo):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='a*70427042',db='moviewatch' ,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,port=8888)
    cur=conn.cursor()
    cur.execute("use moviewatch")
    cur.execute("insert into review(Rno,Ruser,Rstar,Rreview,Review_site_table_Rsite,movie_MNo,user_CNo)VALUES('%d','%s','%d','%s','%d','%d','%d')"%(Rno,Ruser,Rstar,Rreview,Review_site_table_Rsite,movie_MNo,user_CNo)) 
    cur.connection.commit()