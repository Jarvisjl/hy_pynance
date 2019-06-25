# hy_pynance
The purpose of this project is to pull stock index data from tdameritrade's api (and soon alphavantage for real time data) to model stock prices of indices by each minute of the business day. The current version simply displays line plots that model price changes throughout the day for each stock index. The current version takes around 10 seconds to extract, clean, and store a day's worth of data for each index. As of writing this, it takes under 10 seconds to pull the sql data and run the visuals with around 20000 records in a single table.

To use:
-must have a local sql database set up
-use seperate file in another directory to store sensitive information and parameters (or hard code it in)

Features to come:
-automated extraction process
-more metrics and visuals
-user interface (simple guid) with input capability
-real time data
-trading bot? (likely for simulation purposes)
