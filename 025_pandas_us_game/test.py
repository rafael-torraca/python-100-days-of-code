import json
import urllib.request
import pandas as pd

with urllib.request.urlopen("https://data.cityofnewyork.us/resource/vfnx-vebw.json") as url:
    data_json = json.loads(url.read().decode())
    print(data_json)

