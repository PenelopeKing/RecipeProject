"""
Penelope King
April 2022
Recipe Finder Project
"""

import pandas as pd
import numpy as np
from ast import literal_eval
import load_csv

class RecipeFinder:

    df = None
    ing_input = None

    def __init__(self, filepath, ing_input):
        """
        for initializing the class RecipeFinder
        """
        self.ing_input = ing_input

        def mod_NER(NER_list_str):
            '''
            turn string into a list
            modifies so all strings to be lowercase as well
            '''
            to_list = literal_eval(NER_list_str)
            return [item.lower() for item in to_list]

        def get_data(self, fp) -> pd.DataFrame():
            """
            makes dataframe depending on what csv filepath input into function
            input: String of the filepath to dataframes will be using
            outout: panda DataFrame for that csv
            """
            raw_df = pd.read_csv(fp)
            raw_df = raw_df.drop(columns = ['Unnamed: 0'])
            df= raw_df.get(['title','ingredients','link','NER'])
            df['NER'] = df['NER'].apply(mod_NER)
            return df
        
        self.df = get_data(self, filepath)



    def find_recipe(self) -> pd.DataFrame():
        """
        will return a DataFrame of reicpes that matches the input ingredients 
        input: list of ingredients
        return: panda DataFrame (elements of data df that matches ing_list)
        """
        def ing_match(NER_list):
            """
            method intended for a panda series

            """
            checking = all(ing.lower() in self.ing_input for ing in NER_list)
            return checking
        
        self.df['has_ingredients'] = self.df['NER'].apply(ing_match)

        # returns... 
        return self.df[self.df.get('has_ingredients')]

def ask_for_ing():
    """
    asks for input for ingredients
    """
    print('TYPE the ingredients you own one-by-one \
    \n OR type "LOOK" to check what you already inputted in \
    \n OR type "DONE" when you are done inputting your ingredients')

    input_message ='TYPE AN INGREDIENT YOU OWN HERE:  '

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
    return(ing_list)
    '''
    TO DO... 
    double_check = input('Are these the ingredients you have?')
    if (double_check.lower() == 'no') | (double_check.lower() == 'n'):
    '''

def main():
    """
    main method
    """
    # testing class RF

    # ask for input
    ing_list = ask_for_ing()
    filepath = 'datasets/RecipeNLG_dataset.csv'

    # this takes a long time because it loads in the dataset while initializing
    # will need to delegate loading in the dataset in a different file later
    RF = RecipeFinder(filepath, ing_list)
    
    matches = RF.find_recipe()
    print(matches)

