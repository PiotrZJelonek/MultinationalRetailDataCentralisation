import pandas as pd
import numpy as np

# class definition
class DatabaseConnector:
    """
    This class will connect with and upload data to the database.
    """
    # class constructor
    def __init__(self):
        pass


    def read_db_creds():
        """
        Read database credentials from .yaml file
        """
        return pd.read_yaml('config/db_creds.yaml')