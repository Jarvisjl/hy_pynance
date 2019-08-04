# hy_pynance
The purpose of this project is to pull stock index data from tdameritrade's api (and soon alphavantage for real time data) to model the prices of a stock by each minute of the business day. The current version simply displays line plots that model price changes throughout the day for each stock index. Hope to continue updating this readme.

To use:
-must have a local sql database set up
-use seperate file in another directory to store sensitive information and parameters (or hard code it in)

USER INPUT PARAMETERS:
-For stock: research the abbreviation of the stock you wish to visualize. Incorect spelling will lead to an error.
-For metric, choose between: open, close, high, low, volume
-for color (plot), choose between: 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'

Features to come:
-automated extraction process
-more metrics and visuals
-user interface (simple gui) with input capability
-real time data
-trading bot? (likely for simulation purposes)

update (6/29/19):
-added user input with exception handling
-need to do more research on UI in python. The gui in the standard library wasn't well suited for handling user input
    -potentially research web applications (django?), also someone suggested using a recently released microsoft tool for machine learning      (azure ml?), I'll have to learn some ml first..
-renamed all of the classes and just deleted the old classes from github.
