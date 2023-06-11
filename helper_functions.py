import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='akr21001')
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)

# finding the missing values by a specific theresold
def get_missing_values(df,threshold):
    """
    Input:
        Given the dataframe and the threshold, the function will extract the dataframe and then remove the columns with missing value percentage above the threshold.
    
    Output:
        Gives us a list of columns which satisfy the condition.
    
    """
    missing_values = pd.DataFrame((df.isna().sum()/df.shape[0])*100)
    missing_values.reset_index(inplace=True)
    missing_values.rename(columns={'index':'column_name',0:'percentage_of_missing_values'},inplace=True)
    return missing_values.loc[missing_values['percentage_of_missing_values']>threshold,'column_name'].values

# sample row viewer
def get_random_row(df):
    n=np.random.randint(df.shape[0])
    print(df.iloc[n,:])
    

    # converting string to tuple
def convert_string_tuple(n):
    return eval(n)

# cleaning the policy numbers
def cleaning_policy_numbers(df,col = 'POLICY_NUMBER'):
    """
    Input: 
        Given the dataframe and the column name which is the POLICY NUMBER in this instance
    Output:
        Converts the column into 
    """
    df[col] = df[col].astype('str')
    df[col] = df[col].str.zfill(8)
    return df[col]