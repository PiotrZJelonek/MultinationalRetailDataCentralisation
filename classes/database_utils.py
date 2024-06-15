import pandas as pd
import numpy as np
import yaml

# class definition
class DatabaseConnector:
    """
    This class will connect with and upload data to the database.
    """
    # class constructor
    def __init__(self, paths: dict):
        self.paths = paths

    def read_db_creds(self):
        """
        Read database credentials from .yaml file
        """
        # Define the path to your YAML file
        yaml_file = 'db_creds.yaml'
        load_path = self.paths['config'] / 'db_creds.yaml'

        print(load_path)

        # try:
        #     with open(load_path , 'r') as file:
        #         config_dict = yaml.safe_load(file)
        #     print(config_dict)
        # except FileNotFoundError:
        #     print(f"Error: The file {yaml_file} does not exist.")
        # except yaml.YAMLError as exc:
        #     print(f"Error parsing YAML file: {exc}")

        return 0
    