import pandas as pd
import numpy as np
from classes.database_utils import DatabaseConnector

# class definition
class DataExtractor:
    """
    This class will work as a utility class, in it you will be creating methods 
    that help extract data from different data sources.
    """
    # class constructor
    def __init__(self, dc: DatabaseConnector):
    
        self.dc = dc

    # methods
    def read_rds_table(self, table_name: str) -> pd.DataFrame:
        """
        Read data from a table in the database
        """
        return pd.read_sql_table(table_name, self.dc.engine)


    def fetch_csv(self):
        """
        Extract data from .csv files
        """
        pass

    def fetch_api(self):
        """
        Extract data from an API
        """
        pass

    def fetch_s3(self):
        """
        Extract data from an S3 bucket
        """
        pass    
