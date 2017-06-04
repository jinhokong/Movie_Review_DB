import pymysql
def store(Ruser,Rstar,Rreview,Review_site_table_Rsite,movie_MNo,user_CNo):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='a*70427042',db='moviewatch' ,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,port=8888)
    cur=conn.cursor()
    cur.execute("use moviewatch")
    cur.execute("insert into review(Ruser,Rstar,Rreview,Review_site_table_Rsite,movie_MNo,user_CNo)VALUES('%s','%d','%s','%d','%d','%d')"%(Ruser,Rstar,Rreview,Review_site_table_Rsite,movie_MNo,user_CNo)) 
    cur.connection.commit()