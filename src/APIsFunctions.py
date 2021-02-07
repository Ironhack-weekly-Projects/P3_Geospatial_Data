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

coordinates = {'madrid': [-3.6793, 40.42955],
 'bilbao': [-2.9253, 43.2627],
 'gijon': [-5.7258, 43.5317],
 'toledo': [-4.02711, 39.94034]}


def get_coordinates(lista):

    '''
    EXPLICAR LO QUE HACE
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
    EXPLICAR LO QUE HACE
    '''

    dict_empty = {}
    for k, v in c.items():
        coor = [float(v["longt"]),float(v["latt"])]
        dict_empty[k] = coor
    return dict_empty


def get_data (latitude, longitude, *args):
    '''
    descripcion de lo que hace la función aquí
    '''  
    d = {}
    
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
            
        elif key == "Bar":
            bar = result.get(key)
            response = bar.get('response')
            decoded = response.get('groups')[0]
            final_bar = decoded.get('items')

            
        elif key == "Park":
            park = result.get(key)
            response = park.get('response')
            decoded = response.get('groups')[0]
            final_park = decoded.get('items')
            
        elif key == "Athletics & Sports":
            sports = result.get(key)
            response = sports.get('response')
            decoded = response.get('groups')[0]
            final_sport = decoded.get('items')
            
        else:
            train = result.get(key)
            response = train.get('response')
            decoded = response.get('groups')[0]
            final_train = decoded.get('items')
            
    return final_school, final_vegan, final_bar, final_park, final_sport, final_train