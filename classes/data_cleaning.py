import pandas as pd
import numpy as np

# class definition
class DataCleaning:
    """
    This class will contain methods to clean data from each of the data sources.
    """
    # class constructor
    def __init__(self, df: pd.DataFrame):

        self.df = df

    # class methods

    def clean_user_data(self) -> pd.DataFrame:
        """
        Clean user data. 
        Look out for NULL values, errors with dates, incorrectly typed values and rows filled with the wrong information.
        """
        pass

        return self.df

    def clean_payment_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean payment data. 
        Look out for NULL values, errors with dates, incorrectly typed values and rows filled with the wrong information.
        """
        pass


    def clean_movie_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean movie data. 
        Look out for NULL values, errors with dates, incorrectly typed values and rows filled with the wrong information.
        """
        pass