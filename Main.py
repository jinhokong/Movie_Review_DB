import naver
import naver_movie
import rotten
URL = input('Input your movie name : ') 
code=naver_movie.SearchMovieName(URL)   
naver.NaverReview(code)