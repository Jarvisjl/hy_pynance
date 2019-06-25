#hypy_model models the time series data from local sql database
#to-do list:
# -Calculate moving averages
# -research more ways to model
# -include real time data to track (seperate script?)
import pyodbc
import pandas as pd
import numpy as np
import urllib
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'C:/Users/jjarvis/Documents/secrets_params/')
import hypy_params

#Create a completely empty Dataframe without any column names, indices, or data: df
df = pd.DataFrame()

#define engine parameters
params = urllib.parse.quote_plus("DRIVER=ODBC Driver 17 for SQL Server;"
                                 "SERVER={};"
                                 "DATABASE={};"
                                 "Trusted_Connection=yes".format(hypy_params.server,hypy_params.db) 
                                 )
#define engine
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))


#Read the data from SQL into dataframe
query='SELECT  [symbol] AS [company],[open],[close],[high],[low],[volume],DATEADD(ss, CAST(([datetime]-14400000)/1000 AS INT),''1970/01/01'') AS [Date Time] FROM stockIndex'
df = pd.read_sql(query, engine)
df['date'] = pd.to_datetime(df['Date Time'], format='%Y:%M:%D').dt.date
df['time'] = pd.to_datetime(df['Date Time'], format='%Y:%M:%D').dt.time
df = df.drop(columns = ['Date Time'])

#microsoft index time series plot
fig1, ax1 = plt.subplots()
msft_df = df.loc[df['company'] == 'MSFT']
msft_df.groupby(by= "date").plot(x='time', y = 'open', ax=ax1, color = 'y', title = "Microsoft Index", legend =False)

#AT&T index time series plot
fig2, ax2 = plt.subplots()
goog_df = df.loc[df['company'] == 'T']
goog_df.groupby(by= "date").plot(x='time', y = 'open', ax=ax2, color = 'g', title = "AT&T Index", legend =False)

#amazon index time series plot
fig3, ax3 = plt.subplots()
amzn_df = df.loc[df['company'] == 'POL']
amzn_df.groupby(by= "date").plot(x='time', y = 'open', ax=ax3, color = 'r', title = "PolyOne Index", legend =False)

#apple index time series plot
fig4, ax4 = plt.subplots()
aapl_df = df.loc[df['company'] == 'HPE']
aapl_df.groupby(by= "date").plot(x='time', y = 'open', color = 'r', title= "HP Index", ax=ax4, legend =False)

#facebook index time series plot
fig5, ax5 = plt.subplots()
fb_df = df.loc[df['company'] == 'MRO']
fb_df.groupby(by= "date").plot(x='time', y = 'open', ax=ax5,color = 'b', title = "Marathon Index", legend =False)


plt.show()

