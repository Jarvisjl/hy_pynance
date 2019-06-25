#hypy_extract imports stock index data from API into local sql database

import requests
import pandas as pd
import urllib
from sqlalchemy import create_engine
import sys
sys.path.insert(0,'C:/Users/jjarvis/Documents/secrets_params/')
import hypy_params

#list of companies to be used as parameters for getPrices():
#for this instance, hypy_params.stocks1 = ['T', 'POL', 'MSFT','MRO','HPE']
stocks = hypy_params.stocks1

#empty Dataframe w/o any column names, indices, or data to be used later in script: df
df = pd.DataFrame()
 

def get_prices(company):
#uses the TDAmeritrade API to gather historical prices on each company's stock
    
    #define the endpoint
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(company)

    #define the payload, you can change time parameters to your own taste.
    #check 'TDAmeritrade for developers' documentation for more info
    payload = {'apikey':hypy_params.apikey,
               'periodType':'day',
               'frequencyType':'minute',
               'frequency':'1',
               'period':'10',
               'needExtendedHoursData':'false'}
    # make a request
    content = requests.get(url = endpoint, params = payload)

    # return json string
    data = content.json()
    return(data)

#loops through stock list and gathers index data from each, stores into df
for comp in stocks:
    temp_df = pd.DataFrame.from_dict(get_prices(comp), orient='columns')
    df = df.append(temp_df)
    
#split dictionary column, 'candles', into multiple columns
#concatonate df (w/o 'candles' or 'empty') with seperated 'candles' columns
df = pd.concat([df.drop(['candles','empty'], axis=1), df['candles'].apply(pd.Series)], axis=1)

#define engine parameters
params = urllib.parse.quote_plus("DRIVER=ODBC Driver 17 for SQL Server;"
                                 "SERVER={};"
                                 "DATABASE={};"
                                 "Trusted_Connection=yes".format(hypy_params.server,hypy_params.db) 
                                 )
#define engine
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

#insert df into local sql table
df.to_sql('stockIndex', engine, if_exists = 'replace', chunksize = None)



print(df)
    
    