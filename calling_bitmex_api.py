import requests
import pandas as pd

raw_json = requests.get('https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBT&depth=25').json()

data = pd.DataFrame(raw_json)