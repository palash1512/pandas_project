# Default Imports
import pandas as pd
from pandas import DataFrame

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(path_d):
    return DataFrame(pd.read_csv(path_d))
