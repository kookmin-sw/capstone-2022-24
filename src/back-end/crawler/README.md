# Back-end crawler

## Outline

### crawler_base.py
collecting frequently used method and redundantly used variables for crawling
 - check_vaild: checking if the value exists in the dict
 - get_request_to_object : Receiving json data through URL and deserialize it into a python object
 - check_sample: Checking if data already exists

### crawling_TV.py
Based on the crawler_base.py, Crawl Tv Data using API data and Save Tv data

### crawling_movie.py
Based on the crawler_base.py, Crawl Movie Data using API data and Save Tv data

### arrange_data.py
Based on the dict created with crawling_TV.py and crawling_movie.py Be arranged according to the data format to be stored in the actual DB.

### saving_db.py
Save the data arranged through arrange_data.py in the actual DB

### check_env.py
Check the environment and read environment variable file according to the environment.

## folder : discontinue
Folder containing code to crawl information about discontinuing videos


## HOW TO USE?
### 1. select video category that you want.
- there's two category, Tv or movie.

### 2. Go to the Crawler Folder
- **In Linux**
`cd src/back-end/crawler`

- **In Window**
`cd src\back-end\crawler`

### 3. Run the file named Crawling in the category you want.
- crawing_TV.py
- crawling_movie.py

### 4. If you want to save the data saved as a json file in the DB, first Run setting_provider.py

### 5. Run saving_DB.py.
it's done!


## Warning
this version can make an error to update, if the data to be updated already exists in the DB.
