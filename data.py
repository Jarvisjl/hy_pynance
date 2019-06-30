# hypy viz stores functions that plot the projects data
import pandas as pd
import urllib
import requests
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import sys
import datetime
sys.path.insert(0,'C:/Users/jjarvis/Documents/secrets_params/')
import hypy_params


def get_old_data(company):
#Get historical stock index data from TD Ameritrade's API
#uses the TDAmeritrade API
    
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
    print('\npatience my child\n')
    # return json string
    data = content.json()
    #convert to a dataframe
    df = pd.DataFrame.from_dict(data)
    
    #split dictionary column, 'candles', into multiple columns
    #concatonate temp_df (w/o 'candles' or 'empty') with seperated 'candles' columns
    df = pd.concat([df.drop(['candles','empty'], axis=1), df['candles'].apply(pd.Series)], axis=1)
    
    #Probably a simpler way to do this but the original day time format is in unix (4 hours into the future)
    #first set the unix time in ms back by four hours to reflect market hours
    df['datetime'] = df['datetime']-14400000
    #convert it to a datetime object
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms').dt.strftime('%m-%d-%Y , %H:%M:%S')
    #split into date and time seperately for grouping purposes
    df['date'] = pd.to_datetime(df['datetime']).dt.strftime('%m-%d-%Y')
    df['time'] = pd.to_datetime(df['datetime']).dt.strftime('%H:%M:%S')
    #drop original datetime column
    df =df.drop(columns=['datetime'])

    return df

def get_real(company,frq):
#Get real time stock index data from AlphaVantage's API
    ###To do
    return

def mean_plot(dataframe, metric, color,comp):
    fig, ax = plt.subplots()
    dataframe.groupby(by= ['date']).plot(x='time',
                                y = metric,
                                ax=ax,
                                color = color,
                                title = comp + 'last 10 day price movement by time of day',
                                legend =False)
    mean = dataframe.groupby('time')[metric].mean()
    mean.plot(color = 'r', legend=True, label = 'simple average')
    plt.show()


#def calc_ema(dataframe, company, st_date, span):
  #  if(abs(st_date - datetime.today().strftime('%m-%d-%Y')) = span)
     #   df.loc['['ema'] = 
    #calculates ema using tail recursion
     
     