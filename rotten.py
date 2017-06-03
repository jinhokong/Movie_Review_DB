import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
def rotten_tomato(name):
    html =urlopen("https://www.rottentomatoes.com/m/"+name)
    bsObj=BeautifulSoup(html,"html.parser")
    nameList=bsObj.findAll("span",{"class":"meter-value superPageFontColor"})
    for name in nameList:
        print(name.get_text() )
a= input("Name:")
b=a.split(' ')
a="_".join(b)
rotten_tomato(a)
