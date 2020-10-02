import os
import sys
import time
import json
import requests

def movieIds(maxMovies):

	url = 'https://api.themoviedb.org/3/movie/top_rated'	
	tmdb_api_key = os.environ['TMDB_API_KEY']

	tmdb = requests.Session()
	tmdb.params={'api_key':tmdb_api_key}

	global movieIds
	movieIds = []
	num_pages = int(maxMovies / 20)
	
	for page in range(1,num_pages+1):
		httpResp =tmdb.get(url,params={'page':page})
	
		try:
			if int(httpResp.headers['x-ratelimit-remaining']) < 10:
				time.sleep(0.5)
		except Exception as e:
			print(e)

		jsonResponse = json.loads(httpResp.text)
		movies = jsonResponse['results']
		with open('data/moviesid.txt','a') as data_handle:

			for movie in movies:
				data_handle.write(str(movie['id'])+'\n')

	return movieIds

def main():
	movieIds(sys.argv[1])

if __name__ == '__main__':
	main()