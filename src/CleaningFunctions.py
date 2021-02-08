def cleaning (df, col, new_col):
    
    #remove quotes
    df[col] = df[col].str.replace(r"[\"\',]", '')
    
    #remove empty space
    df[col] =  df[col].str.strip()
    
    #delete columns that we are not going to use
    df2 = df.drop(["_id", "loc", "name"], axis = 1)
    
    df2.insert(1, 'city', new_col)
    
    # to reclassify_categorie
    df2 = df2.replace(to_replace=r'Health Food Store|Gym / Fitness Center|Gym', value='Basketball Court', regex=True)
    df2 = df2.replace(to_replace=r'Platform|Train Station', value='Train', regex=True)
    df2 = df2.replace(to_replace=r'Beer Bar|Tapas Restaurant|Brewery|Sandwich Place|Lounge|Pub|Snack Place|Café|Cocktail Bar|Restaurantlt_|Bars', value='Bar', regex=True)
    

    return df2