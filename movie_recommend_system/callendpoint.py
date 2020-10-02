'''
	Call endpointFunction. 
	input: a valid url endpoint.
	process:
		catch status code
		return json response 
'''

import os
import sys
import json
import requests

def callTMDBendPoint(endpoint, _params=None):

	url = 'api_url'+ endpoint
	
	tmdb_api_key = os.environ['TMDB_API_KEY']
	
	tmdb = requests.Session()
	tmdb.params = {'api_key':tmdb_api_key}

	httpQuery = tmdb.get(url,params=_params) 

	return 'done'
