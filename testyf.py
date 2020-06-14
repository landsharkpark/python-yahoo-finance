import yfinance as yf

tickers_list = ['AAPL','MSFT','AMZN','JPM','WFC']

#msft = yf.download('MSFT',start='2020-04-10',end='2020-04-20',progress=False)
#print(msft.head())

data = yf.download(tickers_list,'2020-04-16','2020-04-20')['Adj Close']

print(data.tail())

print(data['MSFT']['Adj Close'])



#print('next test')
#data2 = yf.download(tickers_list,'2020-04-10','2020-04-20')
#print(data2.tail()['Adj Close'])

#print('third test')
#tickerdata = yf.Ticker('MDT')

#tickerinfo = tickerdata.info
#print(tickerinfo)

#tickerDF = tickerdata.history(period='1d',start='2020-04-20',end=today[:10])
#priceLast = tickerDF['Close'].iloc

#print('\n\n\nBank Data\n\n')
#bankdata = yf.download(['JPM','WFC'],start='2020-04-20',end='2020-04-20',progress=False)
#print(bankdata.head())


