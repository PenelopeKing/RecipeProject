"""
Penelope King
April 2022
Recipe Finder Project
"""

import pandas as pd
import numpy as np

class RecipeFinder:

    df = None

    def __init__(self, filepath):
        """
        for initializing the class RecipeFinder
        """
        self.df = self.get_data(filepath)


    def get_data(self, filepath) -> pd.DataFrame():
        """
        makes dataframe depending on what csv filepath input into function
        input: String of the filepath to dataframes will be using
        outout: panda DataFrame for that csv
        """

        raw_df = pd.read_csv(filepath)
        raw_df = raw_df.drop(columns = ['Unnamed: 0'])
        df= raw_df.get(['title','ingredients','link','NER'])
        return df

    def ing_match(self, ings):
        """
        method for dataframe series
        """


    def find_recipe(self, ing_list) -> pd.DataFrame():
        """
        will return a DataFrame of reicpes that matches the input ingredients 
        input: list of Strings (ingredients)
        return: panda DataFrame (elements of data df that matches ing_list)
        """
        self.df.apply(self.ing_match)

# testing class RF
# (!) dataset is extracted from outside of this workspace
    # stored only on my computer for now
filepath='/Users/penelopeking/Desktop/RecipeProject_Data/RecipeNLG_dataset.csv'
RF = RecipeFinder(filepath)

# ask for input

print('TYPE the ingredients you own one-by-one \
\n OR type "LOOK" to check what you already inputted in \
\n OR type "DONE" when you are done inputting your ingredients')

input_message ='TYPE AN INGREDIENT YOU OWN HERE:    '

ing_list = []
not_done = True
while not_done:
    ing_has = input(input_message)
    if (ing_has.lower() == 'done'):
        not_done = False
        break;
    elif (ing_has.lower() == 'look'):
        print(ing_list)
    else:
        ing_list.append(ing_has)

print(ing_list)
'''
double_check = input('Are these the ingredients you have?')
if (double_check.lower() == 'no') | (double_check.lower() == 'n'):
'''

