import requests
from io import StringIO
import pandas as pd
import numpy as np

datestr = '20201126'

# 下載股價
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '})
     for i in r.text.split('\n') 
     if len(i.split('",')) == 17 and i[0] != '='])), header=0)
#set filters
df.to_csv('twse' + datestr + '.csv')
pd.read_csv('twse' + datestr + '.csv')
df.loc[(pd.to_numeric(df['本益比'], errors='coerce') < 15) & (pd.to_numeric(df['本益比'], errors='coerce') > 5) & (pd.to_numeric(df['收盤價'], errors='coerce') < 30) & (pd.to_numeric(df['成交筆數'], errors='coerce') > 100)]
