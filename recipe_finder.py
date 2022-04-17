"""
Penelope King
April 2022
Recipe Finder Project
"""
import pandas as pd
import numpy as np
from ast import literal_eval

class RecipeFinder:
    df = None
    ing_input = None

    def __init__(self, ing_input):
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

        def get_data(self) -> pd.DataFrame():
            """
            makes dataframe depending on what csv filepath input into function
            input: String of the filepath to dataframes will be using
            outout: panda DataFrame for that csv
            """
            df = pd.read_pickle('pickled_data.pkl')
            df = df.drop(columns = ['Unnamed: 0'])
            df= df.get(['title','ingredients','link','NER'])
            df['NER'] = df['NER'].apply(mod_NER)

            # gets rid of the empty lists in the data frame
            df = df[df['NER'].map(lambda x : len(x) > 0)]
            return df
        
        self.df = get_data(self)


    def find_recipe(self) :
        """
        will return a DataFrame of reicpes that matches the input ingredients 
        input: list of ingredients
        return: string outlining what recipes can make -> puts it into a file
        + also modifies original dataframe with a new column "has_ingredients"
            which is TRUE if input list matches it, false otherwise
        """
        def ing_match(NER_list):
            """
            (!) needs improvements

            method intended for a panda series
            finds out if input list has any matches for a row in data frame 
            """
            checking = all(ing.lower() in self.ing_input for ing in NER_list)
            return checking
        
        self.df['has_ingredients'] = self.df['NER'].apply(ing_match)
        
        # only contains enteries where has_ingredients == True
        match_df = self.df[self.df['has_ingredients']].reset_index(drop=True)
        
        # examples for output
        match_1 = (match_df.get('title').iloc[0], \
            match_df.get('ingredients').iloc[0])
        match_2 = (match_df.get('title').iloc[match_df.shape[0]-1], \
            match_df.get('ingredients').iloc[match_df.shape[0]-1])

        with open('my_recipes.txt','w') as rec:
            rec.write('Recipes:\n')
            # (!) this may be slow...
            for i in range(match_df.shape[0]):
                match = (match_df.get('title').iloc[i],\
                     match_df.get('ingredients').iloc[i],\
                     match_df.get('link').iloc[i])
                rec.write('{} : {}\n{}\n'.format(match[0], match[1], match[2]))
        
        # making string for output
        output = '\nI found {} recipes for you!'.format(match_df.shape[0]) + \
        '\nHere are some recipes you can make: \n'+ \
        'Recipe Suggestion 1: {}, which uses {} \
        \nRecipe Suggestion 2: {}, which uses {} \n\
            '.format(match_1[0],match_1[1],match_2[0],match_2[1]) + \
        '\nI put more recipes you can take a look at in this folder!' + \
        '\nCheck out my_recipes.txt to check out even more recipes!'
        return output


def start():
    """
    main method, run this method to start the code
    """
    def ask_for_ing():
        """
        asks for input for ingredients
        """
        input_message ='TYPE AN INGREDIENT YOU OWN HERE:    '
        ing_list = []
        not_done = True
        stuff_to_delete = True
        print('TYPE the ingredients you own one-by-one \
        \n OR type "LOOK" to check what you already inputted in \
        \n OR type "DONE" when you are done inputting your ingredients')
        while not_done:
            ing_has = input(input_message)
            if (ing_has.lower() == 'done'):
                not_done = False
                break;
            elif (ing_has.lower() == 'look'):
                print(ing_list)
            else:
                ing_list.append(ing_has.lower())
        # double checks if user wants to take out anything in their list
        while stuff_to_delete:
            print('\nYOUR INGREDIENTS: ')
            print(ing_list)
            double_check = input('\nAnything you want to delete? (Y/N)  ')
            if (double_check.lower() == 'no') | (double_check.lower() == 'n'):
                delete = input('What do you want to delete?     ')
                ing_list.remove(delete.lower())
            elif (double_check.lower() == 'yes') | (double_check.lower() == 'y'):
                stuff_to_delete = False
        print('\nYOUR INGREDIENTS: ')
        print(ing_list)
        return(ing_list)

    # calling functions here
    # asks for input
    ing_list = ask_for_ing()
    print('\nFinding recipes! This make take a while...\n')

    RF = RecipeFinder(ing_list)
    print(RF.find_recipe())

