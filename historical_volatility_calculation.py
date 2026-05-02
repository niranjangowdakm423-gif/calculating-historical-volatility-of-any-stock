def historical_volatility(name='^NSEI',period_='1y'):
  import yfinance as yf
  import numpy as np
  import math as m
  data = yf.download(name, period=period_)
  closes = data['Close'][name].dropna().tolist()
  log_returns=[]
  for i in range(1,len(closes)):
      r=m.log(closes[i]/closes[i-1])
      log_returns.append(r)
  sigma_daily=np.std(log_returns,ddof=1)
  sigma_annually=sigma_daily*(252)**(0.5)
  return sigma_annually


