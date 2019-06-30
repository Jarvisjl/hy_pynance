#hypy mod models the time series data from local sql database
#to-do list:
# -Calculate moving averages
# -research more ways to model
# -include real time data to track (seperate script?)
import pandas as pd
import urllib
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import sys
import datetime
import auth
import data

#Take user input to set parameters
print('Welcome to hy_pynance. For instructions and valid inputs, see the readme.')
while True:
    try:
        comp = input('Enter stock abreviation: ')
        metric = input('Enter metric: ')
        color = input('Enter a color for the visual: ')
        df = data.get_old_data(comp)
        break
    except Exception as e:    
        pass

    print('\nIncorrect parameters. Learn more on this in the read_me. Try again')
   
#will store data if 'y', does nothing if anything else
get_data = input('Enter "y" if you would like to store data in sql table: ')
if (get_data=='y'):
    engine = viz.get_engine()
    df.to_sql(comp, engine)

#plots
#valid colors =  {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
data.mean_plot(df,metric,color,comp)

