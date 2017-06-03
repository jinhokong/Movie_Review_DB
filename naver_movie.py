import requests
import json
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
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
    #return ("http://movie.naver.com/movie/bi/mi/basic.nhn?code="+final[0])  #해당 영화 사이트 반환
