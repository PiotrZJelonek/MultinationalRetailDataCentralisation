import pandas as pd
import numpy as np

# class definition
class DataExtractor:
    """
    This class will work as a utility class, in it you will be creating methods 
    that help extract data from different data sources.
    """
    # class constructor
    def __init__(self):
        self.value = 7

    # methods
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
