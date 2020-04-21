"""IMPORTS"""
#import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pandas_datareader
import pandas_datareader.data as web
from datetime import date
from pandas.plotting import scatter_matrix


#determines if parts of the code that show plots wil be executed
show_plots = False

"""Analysis Window"""
start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

"""Stock List"""
stock_list = list()
#watch_list = [("Tesla","TSLA"),("GM","GM"),("Ford","F"),("Volkswagen","VWAGY")]


def stock_reader(name,ticker):
    try:
        date_log
    except NameError:
        date_log = None
    file_name = name + ".csv"
    if date_log != date.today():
        date_log = date.today()
        name = web.DataReader(ticker,"yahoo",start,end)
        name.to_csv(file_name)
    name = pd.read_csv(file_name,index_col="Date")
    return name


ford = stock_reader("Ford","F")
gm = stock_reader("GM","GM")
tesla = stock_reader("Tesla","TSLA")

class Stock(object):
    def __init__(self,ticker,friendly_name):
        self.friendly_name = friendly_name
        self.ticker = ticker
        self.data = stock_reader(ticker,ticker)
        stock_list.append(self)

honda = Stock("HMC","Honda")


"""Import Data on Stocks"""
#for stock in watch_list:


#tesla = stock_reader("tesla","TSLA")
#ford = stock_reader("ford","F")
#gm = stock_reader("gm","GM")

#print(tesla.info())

"""Total Traded Calculations"""
ford["Total Traded"] = ford["Open"] * ford["Volume"]
gm["Total Traded"] = gm["Open"] * gm["Volume"]
tesla["Total Traded"] = tesla["Open"] * tesla["Volume"]
#for stock in stock_list:


#print(ford.head())


gm["50 Day MA"] = gm["Open"].rolling(50).mean()
gm["200 Day MA"] = gm["Open"].rolling(200).mean()

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
    ford["Total Traded"].plot(label="Ford",figsize=(16,8),title="Total Traded Value")
    tesla["Total Traded"].plot(label="Tesla")
    gm["Total Traded"].plot(label="GM")
    plt.legend()
    plt.show()

#gm[["Open","50 Day MA","200 Day MA"]].plot(label="GM",figsize=(16,8),title="50 day and 200 day MA")
#plt.legend()
#plt.show()
print(tesla["Total Traded"].max())
#print(tesla["Total Traded"].value.argmax())
#print(tesla["Date"][max_value])
print(tesla.index[tesla["Total Traded"].values.argmax()])
car_companies = pd.concat([tesla["Open"],gm["Open"],ford["Open"]], axis = 1)
car_companies.columns = ["Telsa Open", "GM Open", "Ford Open"]
#scatter_matrix(car_companies,figsize=(10,8),alpha=0.3)
#plt.show()

tesla["Returns"] = tesla["Close"].pct_change(1)
ford["Returns"] = ford["Close"].pct_change(1)
gm["Returns"] = gm["Close"].pct_change(1)

show_plots2 = False
if show_plots2 == True:
    ford["Returns"].hist(bins=100,label="Ford",alpha=0.4)
    tesla["Returns"].hist(bins=100,label = "Tesla",alpha=0.4)
    gm["Returns"].hist(bins=100,label="GM",alpha=0.4)
    plt.legend()
    plt.show()
show_plots3 = True
if show_plots3 == True:
    boxdf = pd.concat([tesla["Returns"],ford["Returns"],gm["Returns"]],axis=1)
    boxdf.columns = ["Tesla Returns", "Ford Returns", "GM Returns"]
    boxdf.plot(kind="box", figsize=(8,7))
    plt.show()
    #scatter_matrix(boxdf,figsize = (7,7), alpha = 0.2, hist_kwds = {"bins":100})
    #plt.show()
    boxdf.plot(kind = "scatter", x = "Ford Returns", y = "GM Returns", alpha = 0.3, figsize = (7,7))
    plt.show()
    tesla["Cumulative Return"] = (1+tesla["Returns"]).cumprod()
    ford["Cumulative Return"] = (1+ford["Returns"]).cumprod()
    gm["Cumulative Return"] = (1+gm["Returns"]).cumprod()
    tesla["Cumulative Return"].plot(label="Telsa",title="Cumulative Returns")
    ford["Cumulative Return"].plot(label="Ford")
    gm["Cumulative Return"].plot(label="GM")
    plt.legend()
    plt.show()
