"""
Penelope King
April 11, 2022
Recipie Finder Project
"""

import pandas as pd
import numpy as np

class RecipeFinder:

    df = None

    def __init__(self, filepath : str):
        """
        
        """
        self.df = self.get_data(filepath)


    def get_data(filepath: str) -> pd.DataFrame():
        """
        makes dataframe depending on what csv filepath input into function
        input: String of the filepath to dataframes will be using
        outout: panda DataFrame for that csv
        """

        raw_df = pd.read_csv(filepath)
        raw_df = raw_df.drop(columns = ['Unnamed: 0'])
        df= raw_df.get(['title','ingredients','link','NER'])
        return df


    def ing_match(ing : str):
        """
        
        """


    def find_recipe(ing_list : list) -> pd.DataFrame():
        """
        will return a DataFrame of reicpes that matches the input ingredients 
        input: list of Strings (ingredients)
        return: panda DataFrame (elements of data df that matches ing_list)
        """


# testing class RF

filepath = 'datasets/recipe_nlg/RecipeNLG_dataset.csv'
RF = RecipeFinder(filepath)


