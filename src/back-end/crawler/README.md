# Back-end crawler Data

## crawler_base.py
collecting frequently used method and redundantly used variables for crawling
 - check_vaild: checking if the value exists in the dict
 - get_request_to_object : Receiving json data through URL and deserialize it into a python object
 - check_sample: Checking if data already exists


## crawling_TV.py
Based on the crawler_base.py, Crawl Tv Data using API data and Save Tv data


## crawling_movie.py
Based on the crawler_base.py, Crawl Movie Data using API data and Save Tv data


## arrange_data.py
Based on the dict created with crawling_TV.py and crawling_movie.py Be arranged according to the data format to be stored in the actual DB.


## saving_db.py
Save the data arranged through arrange_data.py in the actual DB
