'''
Made in LabCinf2020-EIB.

This script belog to the stage COLLECT DATA in the Data Life Cycle Model for MvRecSys.

Script Def.: Collect data for a  particular movie id in TMDB Movie DataBase.
	
	Variables Types: ... describe later...

	Objects: Types: ... describe later...

	Funtions:

		getMovieDataById:

			Inputs: movie_id (int.).
			Process: query url_endPoint "movie data" 
		   			through TMDB Api Service.
	   		Output: movie_json (json.).

	   	...
	
'''


import os		# operating system: eg.environment variables                    
import sys      # system utils: eg. std. input												
import json     # data format structures  
import time 	# proccess utils: time requests
import requests # http request: eg. get and post methods
 
#Variables
tmdb_api_key = os.environ['TMDB_API_KEY']

def getMovieDataById(movie_id, tmdb_api_key=tmdb_api_key):
	
	url_endPoint = 'https://api.themoviedb.org/3/movie/%s?api_key=%d' % (movie_id, tmdb_api_key) # url endPoint for request movie data by movie id. (%s). String Formatting C-Stylish.

	tmdb_api = requests.Session()				# python webserver instance.
	tmdb_api.params={'api_key':tmdb_api_key}	# load info into instance. For implicit post method.

	httpResp=tmdb_api.get(url_endPoint)         # query url_endPoint through get method.Is not necessesary params variable.
	
	if httpResp.status_code == 200:             # catch and handle response. v.1
		print('movie_id_ok')
	else: 
		print('bad movie_id',movie_id)
	
	global data
	data = json.loads(httpResp.text)

	#print(data)
	return data

'''
Implement later, with base class exceptions instances. 

def get_movies_data(num_movies):

	cont=0
	_continue_ = True

	while _continue_:

		get_movie_data(cont)
		
		time.sleep(0.5)
		cont+=1

		if status_code==404:
			print(cont,'movie_id not found')
		if cont==num_movies:
			_continue_ = False'''
	

def main():
	print(sys.argv[1])
	get_movie_data(sys.argv[1])

if __name__ == '__main__':
	main()