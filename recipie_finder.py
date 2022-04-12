"""
Penelope King
April 11, 2022
Recipie Finder Project
"""

import pandas as pd
import numpy as np


def process_data(filepath: str) -> pd.DataFrame():
    """
    
    """
    raw_df = pd.read_csv(filepath)
    raw_df = raw_df.drop(columns = ['Unnamed: 0'])
    return raw_df


