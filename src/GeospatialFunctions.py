from pymongo import MongoClient
import pandas as pd
import geopandas as gdp
import shapely
import json
from bson.json_util import dumps


def create_geoloc(path_csv):
    '''
    Receives a path and returns  a dataframe with a new column with the geopoints.
    Args:
        Path : of the csv file containing information about the coordinates and names of all information downloaded from the API
    
    Return:
        Dataframe: with one more column with the geopoints
    '''
    
    #recibe el dataframe
    df = pd.read_csv(path_csv)
    
    #Crea el loc con los geopuntos.
    gdf = gdp.GeoDataFrame(df, geometry= gdp.points_from_xy(df.longitud, df.latitud ))
    gdf.columns=['name', 'lat','long','category','loc' ]
    
    #Lo aplicamos a toda la columna
    gdf['loc']= gdf['loc'].apply(lambda x:shapely.geometry.mapping(x))
   
    return gdf


def queries_close (collection, lon, lat):
    query = [{
    "$geoNear": {'near': [lon, lat],
                 'distanceField': 'distance',
                 'maxDistance': 7000,
                 'distanceMultiplier': 6371, 
                 'spherical'  : True}}]
    geoloc = collection.aggregate(query)
    response_json = json.loads(dumps(geoloc))
    
    return response_json

def check_results(json):
    '''
    Check the results of the geoquerie
    Args: 
        json file: with the information of the geoqueri
    Return:
        A message with the results obtained in the geoquerie
    '''
    results_list = list(json)
    
    if len(results_list) > 0:
        response = {"number of registers" : len(results_list),
                    "datos" : json}
        return (f"Nice! we have found  {len(results_list)}  results")
    else:
        return "Sorry, wa can´t find your petition"
        

