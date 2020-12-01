'''
     catch status code from calls
'''
def catch_error(response):
        if response.status_code == 404:
                print("error 404, what does meant")
        else if response.status_code = "other code":
                print("something went wrong")
	
if __name__ == '__main__':
	

