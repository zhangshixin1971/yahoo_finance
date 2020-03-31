import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
info=msft.info
print(info)

# get historical market data
hist = msft.history(period="max")

print(hist)

# show actions (dividends, splits)
actions=msft.actions
print(actions)

# show dividends
dividends=msft.dividends
print(dividends)

# show splits
splits=msft.splits
print(splits)

# show financials
financials=msft.financials
q_financials=msft.quarterly_financials
print(financials)
print(q_financials)

# show major holders
holders=msft.major_holders
print(holders)

# show institutional holders
msft.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
options = msft.options
print(options)

# get option chain for specific expiration
opt = msft.option_chain('2020-04-02')
print(opt)
# data available via: opt.calls, opt.puts
