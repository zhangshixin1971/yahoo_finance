import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

msft = yf.Ticker("MSFT")

# get stock info
#print(msft.info)

# get historical market data
hist = msft.history(period="1y")
#print(hist)


# Plot everything by leveraging the very powerful matplotlib package
hist['Close'].plot(figsize=(16, 9))

# Download stock data then export as CSV
data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
data_df.to_csv('aapl.csv')

# Change period to last full year
msft.history(period="1y")

# show actions (dividends, splits)
print(msft.actions)

# Results
# Date		    Dividends	Stock Splits
# 2019-05-15	     0.46	         0.0
# 2019-08-14	     0.46	         0.0
# 2019-11-20	     0.51	         0.0
# 2020-02-19	     0.51	         0.0

#Arguments	Scenarios	Example value
#period	date period to download	1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
#interval	data interval. If it’s intraday data, the interval needs to be set within 60 days	1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
#start	If period is not set- Download start date string (YYYY-MM-DD) or datetime	2020-03-18
#end	If period is not set - Download end date string (YYYY-MM-DD) or datetime	2020-03-19
#prepost	Boolean value to include Pre and Post market data	Default is False
#auto_adjust	Boolean value to adjust all OHLC	Default is True
#actions	Boolean value download stock dividends and stock splits events	Default is True