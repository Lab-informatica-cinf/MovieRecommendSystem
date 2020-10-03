'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Directory Structure for Informatic Program "MOVrecommenderlabCinf".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root/
	-definitions
	-requeriments
	-programm setups
	
	src/
		-source code
			modules
			packages(for this project one packages is a RDM fase, under a programatically point of view)
						
	tests/
		- unit test of modules(e.g. modules belong to a some package)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Execution programm PATH(aceptable fiction examples).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

$python3 root/src/MovieRecommenderSystem/load_user_data_module.py input_user_data.json | python3 root/src/MovieRecommenderSystem/main_module.py


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
directory structure project(in building...).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
MovieRecommendSystem/
	README.md
	requeriments.txt
	setup.py
	
	src/
		MovieRecomemendSystem
			__init__.py
      load_user_data.py
			main_module.py
			module.py

			myPkg1/
				__init__.py
				my_module.py
				my_third_module.py

			collectData/                     #our collectDataPakage *.*
				__init__.py
				make_url_end_point_url_.py
				call_tmdb_api.py
				handler_resp_status_code.py
				write_json_results.py

			dataAnalisis/
				__ini__.py
				read_Txt_Data.py
				read_Json_Data.py
				process_Data.py
				
			dataReports/
					#...
									
	tests/
		conftest.py
		
    test_load_user_data.py
		
    collectData/
			test_make_url_end_point.py
		
		analice/
			test_read_txt_data.py			
	'''
