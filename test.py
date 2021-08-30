import yfinance as yf
data = yf.download(tickers_list,'2021-05-3')['Adj Close']

# Print first 5 rows of the data
# print(data.head())
print(data)
