'''
To load CSV file data
Please run this file first before running other code in the file
'''
'''
import requests
# kaggle datasets download -d paultimothymooney/recipenlg
# https://www.kaggle.com/datasets/paultimothymooney/recipenlg?resource=download
# response = requests.get("kaggle datasets download -d paultimothymooney/recipenlg")
response = requests.get("https://www.kaggle.com/datasets/paultimothymooney/recipenlg?resource=download")
print(response.status_code)

if (response.status_code == 200):
    data = response.json()
'''
import pandas as pd
import numpy as np

filepath = 'datasets/RecipeNLG_dataset.csv'
raw_df = pd.read_csv(filepath)
