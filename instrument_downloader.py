import pandas as pd
# Download the CSV file from the URL
fileUrl ='https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz'
symboldf = pd.read_csv(fileUrl)
symboldf['expiry'] = pd.to_datetime(symboldf['expiry']).apply(lambda x: x.date())   
symboldf.to_csv('upstox_instruments.csv', index=False)