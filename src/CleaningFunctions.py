def cleaning (df, col, new_col):

    '''
    Clears the dataframe

    Args: 
        df (dataframe): the dataset to be cleaned
        col : the column we want to apply the cleaning process
        new_col : in this process we generate one new column, here we specify their name

    Returns:
        Dataframe cleaned
    '''
    
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


def weights (row):
    '''
    Generates a new column with the values of the weights I have assigned to each of the parameters obtained from the foursquare API.

    Args:
        row: each row along the dataframe
    Returns:
        dataframe with a new column containing the values of the weights
    '''
    if row['category'] == "Bar":
            val = 0.3
    elif row['category'] == "Basketball Court" :
            val = 0.1
    elif row['category'] == "Preschool" :
            val = 0.1
    elif row['category'] == "Train" :
            val = 0.3
    else:
            val = 0.2
    return val
    
def normalization(df, column):
    '''
    Function that normalize the distance column of the dataframe.
    Args:
        df (dataframe): the dataframe that we want to use to normalize de data
        column (dataframe column): the specific column on which we want to apply the function
    Returns:
        df(dataframe): a dataframe with a new columns with the normalization data
    '''

    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())     
  
    df = df.reset_index(drop = False)
    return df