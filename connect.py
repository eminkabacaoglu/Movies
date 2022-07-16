import requests
import json

class Movies:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3/"
        self.api_key="8e95e822687ed617937400b9413a17f2"
    
    def topRatedMovies(self):
        response=requests.get(self.api_url+"movie/top_rated?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()
    

    def upComingMovies(self):
        response=requests.get(self.api_url+"movie/popular?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()

    def nowPlayingMovies(self):
        response=requests.get(self.api_url+"movie/now_playing?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()    


    def searchMovieByName(self,keyword):
        response=requests.get(self.api_url+"search/movie?api_key="+self.api_key+"&language=en-US&query="+keyword+"&page=1&include_adult=false")
        return response.json()

        