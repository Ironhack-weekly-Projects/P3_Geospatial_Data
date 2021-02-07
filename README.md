# P3_Geospatial_Data
![portada](https://www.acquia.com/sites/acquia.com/files/styles/desktop_hero_image_1x/public/images/2017-12/GettyImages-838600642.jpg?itok=kXtdMcha)

# Objetive
The objective of this project is to determine the perfect location for a new company in the gaming industry. 

- **Designers** --> near to companies that do design.
- **30% of the company** --> have at least 1 child.
- **Developers** --> to be near tech startups that have raised at least 1 Million dollars.
- **Executives** --> like Starbucks.
- **Account managers** --> travel a lot.
- **Average age between 25 and 40** -->some place to go party.
- **CEO** --> vegan.
- **Maintenance guy** --> basketball court
- **Dog—"Dobby"** --> hairdresser every month. 

Based on all the information given by the employees, the first filters I applied to look for possible locations were:
 1. Spanish companies.
 2. In the web sector to be surrounded by companies that are in a similar sector to ours.
 3. With less than 50 employees, to be surrounded by small companies like us
 4. Created since 2007 to be surrounded by young companies. 

# Working plan

![workingplan](https://github.com/AnaAGG/P3_Geospatial_Data/blob/main/Images/Presentaci%C3%B3n1.jpg?raw=true)

The following resources have been used to achieve the objective of this project: 

-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.


### Structure of the project files

The structure of this project is composed of:
 1. A folder of notebooks: 
    
    a) **Explore_Companies.ipynb** -->with the preliminary analysis where I search for companies that meet the requirements established a priori to be able to pre-select locations. 

    b) **APIs.ipynb** --> the call is made to the Api of "Foursquare Developers", where we will get some preferred conditions where we want our company to be located. 

    c) **Geospatial queries.ipynb** --> we make the spatial queries to calculate the distance between each point obtained in the Foursquare API and the locations selected at the beginning. 

 2. scr folder: folder where all the .py files are stored with all the explained functions used during the whole project. 

 3. Output: all the dataframes imported and saved in csv format. 


# Libraries
[import requests](https://pypi.org/project/requests/2.7.0/)

[import pandas as pd](https://pandas.pydata.org/)

[from dotenv import load_dotenv](https://pypi.org/project/python-dotenv/)

[from pymongo import MongoClient](https://www.mongodb.com/2)

[import json](https://docs.python.org/3/library/json.html)

[import os](https://docs.python.org/3/library/os.html)

[import geopandas as gdp](https://geopandas.org/)

[import shapely](https://pypi.org/project/Shapely/)


[from functools import reduce](https://docs.python.org/3/library/functools.html)

import operator

[from bson.json_util import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)