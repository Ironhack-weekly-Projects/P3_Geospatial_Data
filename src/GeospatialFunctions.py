from pymongo import MongoClient
import pandas as pd
import geopandas as gdp
import shapely
import json
from bson.json_util import dumps


def create_geoloc(path_csv):
    '''
    lo que hace
    '''
    
    #recibe el dataframe
    df =pd.read_csv(path_csv)
    
    #Crea el loc con los geopuntos.
    gdf = gdp.GeoDataFrame(df, geometry= gdp.points_from_xy(df.longitud, df.latitud ))
    gdf.columns=['name', 'lat','long','loc']
    
    #Lo aplicamos a toda la columna
    gdf['loc']= gdf['loc'].apply(lambda x:shapely.geometry.mapping(x))
   
    return gdf


