import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list=["MSFT", "APPL"]
today = date.today()
# We can get data by our choice by giving days bracket
start_date = '2010-01-01'
end_date = '2016-12-31'
files=[]
def getData(ticker):
    print (ticker)
    print(start_date,end_date)
#    data = pdr.get_data_yahoo(ticker, start='2019–01–03', end='2019–11–30')
    panel_data = data.DataReader('INPX', 'yahoo', start_date, end_date)
    print(panel_data)
    dataname= ticker+'_'+date.today()
    files.append(dataname)
    SaveData(panel_data, dataname)
# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv('./data/'+filename+'.csv')
#This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
for tik in ticker_list:
    getData(tik)
for i in range(0,11):
    df1= pd.read_csv('./data/'+ str(files[i])+'.csv')
    print (df1.head())
