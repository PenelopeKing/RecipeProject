'''
To load CSV file data
Please run this file first before running other code in the file
You should only need to run once ever
'''
import zipfile
import pandas as pd

# import in CSV with Kaggle API
# https://www.kaggle.com/datasets/paultimothymooney/recipenlg?resource=download
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_file('paultimothymooney/recipenlg', \
    file_name = 'RecipeNLG_dataset.csv' ,  path='./datasets/')

# unzips file
with zipfile.ZipFile('datasets/RecipeNLG_dataset.csv.zip','r') as zipref:
    zipref.extractall('./datasets/')

# csv to panda dataframe
filepath = 'datasets/RecipeNLG_dataset.csv'
raw_df = pd.read_csv(filepath)

# turns dataframe into a pickle file for easier access later on
raw_df.to_pickle("pickled_data.pkl")
