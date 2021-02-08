import requests 
import json
import os
import pandas as pd
from dotenv import load_dotenv

from functools import reduce
import operator
import geopandas as gdp
import shapely


from pymongo import MongoClient

token1= os.getenv("token1")
token2 = os.getenv("token2")

def get_coordinates(lista):

    '''
    Receives a list of localities and returns a dictionary with the coordinates and altitude information of the localities. 
    Args:
        List: with the name as string of the target localities. 

    Return:
        Dicctionary:  with localities and cartographic infomation (altitude, elevation, longitude, latitude)
    '''
    d = {}
    try: 
        for country in lista:
            locations = requests.get(f'https://geocode.xyz/{country}?json=1')
            locations = locations.json()
            d[country] = locations
    except:
        return "Error getting data"
        
    return d

def extract_coordinates(dictionary):

    '''
     Receives a dictionary of localities 
     Args:
        Dictionary: with cartogrphic information
     Returns:
        Dictionary: key = the studies locations, values: latitude and longitude.
    '''

    dict_empty = {}
    for k, v in dictionary.items():
        coor = [float(v["longt"]),float(v["latt"])]
        dict_empty[k] = coor
    return dict_empty


def get_data (latitude, longitude, url_query, *args):
    '''
    Makes the call to the foursquare API to extract the information from the queries we determine.
    Args:
        latitude and longitude (float): the lat and long of the location
        url_query (string): the url of foursquare API
        *args (list): list of the target Venue Category of foursquare
    Return: 
        data (dictionary): a dicctionary with all the information of the Venues per location
    '''  
    d = {}
    token1= os.getenv("token1")
    token2 = os.getenv("token2")
    
    for i in args: 
        parametros = {"client_id" : token1,
                  "client_secret" : token2,
                  "v": "20180323",
                  "ll": f"{latitude},{longitude}", 
                  "query":i,
                  "limit": 100}  

        resp = requests.get(url= url_query, params=parametros)
        data = json.loads(resp.text)        
        d[i] = data
        
    return d

def clean_data(result):
    '''
    It receives a dictionary containing all the information of the API call for each element of the querie and returns a list of dictionaries
    where each one of them is the data of a querie. 
    Args:
        result (list of diccionaries): contain all the infomation of a querie per location
    Return:
        A list of dictionaries. 
    '''


    for key, values in result.items():
        
        if key == "Preschool":
            school = result.get(key)
            response = school.get('response')
            decoded = response.get('groups')[0]
            final_school = decoded.get('items')

        elif key == "Vegan Restaurant":
            vegan = result.get(key)
            response = vegan.get('response')
            decoded = response.get('groups')[0]
            final_vegan = decoded.get('items')
            
            
        elif key == "Beer Bar":
            bar = result.get(key)
            response = bar.get('response')
            decoded = response.get('groups')[0]
            final_bar = decoded.get('items')
            
        elif key == "Basketball Court":
            sports = result.get(key)
            response = sports.get('response')
            decoded = response.get('groups')[0]
            final_sport = decoded.get('items')
            
        else:
            train = result.get(key)
            response = train.get('response')
            decoded = response.get('groups')[0]
            final_train = decoded.get('items')
            
    results = [final_school, final_vegan,  final_bar, final_sport, final_train]
            
    return results

def getFromDict(diccionario,mapa):
    return reduce (operator.getitem,mapa,diccionario)

def create_dataframe (*args):
    '''
    Converts a list of dictionaries with all the information from API calls into a dataframe with the 
    information we want (longitude, latitude, business name and category).

    Args:
        list of dicctionaries with the API information per location

    Return:
        Dataframe: with ordenated infomation
    '''
    mapa_nombre = ["venue","name"]
    m_latitud = ["venue","location","lat"]
    m_longitud = ["venue","location","lng"]
    m_category = ["venue", "categories"]
    
    results = []

    for i in args:
        for dic in i:            
            paralista = {}
            paralista["name"] = getFromDict(dic,mapa_nombre)
            paralista["latitud"] = getFromDict(dic,m_latitud)
            paralista["longitud"] = getFromDict(dic,m_longitud)
            paralista["category"] = getFromDict(dic,m_category)
            results.append(paralista)
    df = pd.DataFrame(results)

    return df

