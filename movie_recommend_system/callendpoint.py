import os
import sys
import json
import requests

#We need one function called make_end_point. build it!

def call_TMDB_end_point(endpoint, _params=None):
'''
	Call end point in TMDB resource. 
	Input: a valid url endpoint.
	Process:
	
        if params:
                end_point = make_end_point(endpoint, _params)
                tmdb_end_point = parametrize_api_connec()
                
        else:
                end_point = make_end_point(end_point)
                tmdb_end_point = parametrize_api_connect(end_point)

        # Call api and handle response

        try:
            response = tmdb.get(_end_point)
            response.raise_for_status
            
        except resquests.exceptions.someError as errh:
            return errh
        except resquests.exceptions.someError as errh:
            return errh
        ...

        data_related_to_movie = response.text
                
'''
        pass
	return data_related_movie

