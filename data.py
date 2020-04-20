"""IMPORTS"""
import numpy as np
import pandas as pd
import quandl
import datetime
import matplotlib.pyplot as plt
import pandas_datareader
import pandas_datareader.data as web

#determines if parts of the code that show plots wil be executed
show_plots = False

"""Analysis Window"""
start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

"""Import Data on Stocks"""
tesla = quandl.get("WIKI/TSLA")
tesla = web.DataReader("TSLA","yahoo", start, end)
ford = web.DataReader("F","yahoo",start,end)
gm = web.DataReader("GM","yahoo",start,end)
print(tesla.head())
print(tesla.info())
ford.head()
#tesla["Date"] = tesla["Date"].apply(pd.to_datetime)
#print(tesla.info())

"""Total Traded Calculations"""
ford["Total Traded"] = ford["Open"] * ford["Volume"]
gm["Total Traded"] = gm["Open"] * gm["Volume"]
tesla["Total Traded"] = tesla["Open"] * tesla["Volume"]
#print(ford.head())

"""Plots"""
if show_plots == True:
    #Comparision of opening prices
    tesla["Open"].plot(label="Telsa",figsize=(12,8),title="Opening Prices")
    gm["Open"].plot(label="General Motors")
    ford["Open"].plot(label="Ford")
    plt.legend()
    plt.show()
    #comparison of volume
    tesla["Volume"].plot(label="Telsa",figsize=(12,8),title="Daily Volume")
    gm["Volume"].plot(label="General Motors")
    ford["Volume"].plot(label="Ford")
    plt.legend()
    plt.show()
    #comparison of total traded value
    ford["Total Traded"].plot(label="Ford",figsize=(16,8))
    tesla["Total Traded"].plot(label="Tesla")
    gm["Total Traded"].plot(label="GM")
    plt.legend()

print(tesla["Total Traded"].max())
print(tesla["Total Traded"].argmax())
