import naver
#import rotten
URL = input("Input movie name: ")
code=naver.SearchMovieName(URL)   
naver.NaverReview(code)