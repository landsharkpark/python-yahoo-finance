import yfinance as yf

tickers_list = ['AAPL','MSFT','AMZN','JPM','WFC']

#msft = yf.download('MSFT',start='2020-04-10',end='2020-04-20',progress=False)
#print(msft.head())

data = yf.download(tickers_list,'2020-04-10','2020-04-20')['Adj Close']

print(data.tail())

print('next test')
data2 = yf.download(tickers_list,'2020-04-10','2020-04-20')
print(data2.tail()['Adj Close'])

print('third test')
tickerdata = yf.Ticker('MDT')

tickerinfo = tickerdata.info
print(tickerinfo)

