import yfinance as yf

def displayresults(tickersymbol):
  alltickerdata = yf.Ticker(tickersymbol)
  tickerinfo = alltickerdata.info
  print('***********************************************')
  print('')
  print('  Company Name: ' + tickerinfo['shortName'])
  print('  Yesterday Close: ' + str(tickerinfo['previousClose']))
  print('  Dividend Yield: ' + str(tickerinfo['dividendYield']))
  print('  Forward P/E: ' + str(tickerinfo['forwardPE']))
  print('  Forward EPS: ' + str(tickerinfo['forwardEps']))
  print('  52 Week High: ' + str(tickerinfo['fiftyTwoWeekHigh']))
  print('  52 Week Low: ' + str(tickerinfo['fiftyTwoWeekLow']))
  print('  50 Day Average: ' + str(tickerinfo['fiftyDayAverage']))
  print('  200 Day Average: ' + str(tickerinfo['twoHundredDayAverage']))
  print('')
  print('***********************************************')
  print('')
  print(tickerinfo)
 
displayresults('MDT')




#msft = yf.Ticker('MSFT')
#tickerinfo= msft.info
#print(tickerinfo['fiftyTwoWeekHigh'])


#msft = yf.Ticker('MSFT')

#msft = yf.download('MSFT')

#print(msft.tail())

#print(msft.info)

#hist = msft.history(period="5d")

#print(hist)

