import urllib.request
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import naver_movie
import pymysql
def NaverReview(CODE):
    total=0
    Rid=0
    url1='http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
    url2='&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
    #f = open('review_'+code+'.txt', 'w')
    page = int(1)
    #count = int(input('Page Number : '))  
    count=10
    conn = pymysql.connect(host='127.0.0.1',user='root',password='a*70427042',db='moviewatch' ,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,port=8888)
    cur=conn.cursor()
    cur.execute("use moviewatch")

    while count: 
        URL = url1+CODE+url2+str(page)
        open_url = urlopen(URL)
        html=open_url.read()
        soup = BeautifulSoup(html,"lxml")
        score_result = soup.find('div',class_='score_result')
        lis = score_result.find_all('li')
        for li in lis:
            page = int(page)
            name = li.find('div',class_='score_reple').findAll('span')
            if(len(name)!=1):
                rank=li.find('div',class_='score_reple').find('span').get_text()
                if(len(name)==2):
                    name=str(name[1])
                    name=name[6:-7]
                elif(len(name)==3):
                    name=str(name[2])
                    name=name[6:-7]
            else:
                rank=None
                name = li.find('div',class_='score_reple').find('span').get_text()
            reple = li.find('div',class_='score_reple').find('p').get_text()
            score = li.find('div',class_='star_score').find('em').get_text()
            score=int(score)
            children = li.find('dt')
            child = children.findChildren()
            time = str(child[3])
            time_s = time[4:17]
            Rid=Rid+1
            print(name)
            print (reple)
            print (score)
            print (time_s)
#            cur.execute("insert into review(Rno,Ruser,Rstar,Rreview) VALUES(\"%d\",\"%s\",\"%d\",\"%s\")"(Rid,name,score,reple))
            cur.execute("insert into review(Rno,Ruser,Rstar,Rident,Rreview,Rsite,favorite_FNo) VALUES('%d','%s','%d','%d','%s','%d','%d')" %(Rid,name,score,Rid,reple,1,Rid))
            cur.connection.commit()
#            f.write('time : ' + time_s + '\t')             
#            f.write('score : ' + score + '\n')
#            f.write('review : ' + reple + '\t')  
        count -= 1
        if not count:
            break
        page += 1  
        total=total+int(score)
    print(total/len(lis))
   # f.close()
URL = input("Input movie name: ")
code=naver_movie.SearchMovieName(URL)   
NaverReview(code)