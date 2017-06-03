import urllib.request
from urllib.request import urlopen
import re
from urllib.parse import quote
from bs4 import BeautifulSoup
import pymysql
import dbstore
def NaverReview(CODE):
    total=0
    Rid=0
    url1='http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
    url2='&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
    page = int(1)
    count=10#review page count
    dbstore


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
            dbstore.store(Rid,name,score,Rid,reple,1,Rid)
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
def SearchMovieName(input):
    input1=quote(input)     #url 코드 인코딩
    url="http://auto.movie.naver.com/ac?q_enc=UTF-8&st=1&r_lt=1&n_ext=1&t_koreng=1&r_format=json&r_enc=UTF-8&r_unicode=0&r_escape=1&q="+input1
    url_to_re=re.compile('\["[0-9]+"\]\,\["movie"\]')   #원시코드에서 정규표현식
    re_to_re=re.compile('[0-9]+')   #정규표현식에서 정규표현식
    m=urlopen(url)  #url 불러옴
    msg=m.read()    #url 읽음
    links=url_to_re.findall(str(msg))   #1차 정규표현식 적용
    final=re_to_re.findall(str(links)) #2차 정규표현식 적용
    return final[0]
URL = input("Input movie name: ")
code=SearchMovieName(URL)   
NaverReview(code)
