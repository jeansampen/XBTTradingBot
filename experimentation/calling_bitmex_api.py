import requests
import pandas as pd
raw_json = requests.get('https://www.bitmex.com/api/v1/trade/bucketed?binSize=1m&partial=false&symbol=XBT&count=1000&reverse=true').json()



data = pd.DataFrame(raw_json)
data.to_csv('bitmex_api_data/trade_bucketed.csv')