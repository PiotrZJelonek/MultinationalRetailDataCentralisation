import pandas as pd
import numpy as np
import yaml
from typing import Optional
from loguru import logger

from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy import inspect


# class definition
class DatabaseConnector:
    """
    This class will connect with and upload data to the database.
    """
    # class constructor
    def __init__(self, paths_dict: dict, verbose: Optional[bool] = True):

        # define fields
        self.paths_dict = paths_dict
        self.db_creds_dict = None
        self.engine = None
        self.tables_list = []
        
        # read password and database credentials
        yaml_files_list = ['postgres_creds.yaml', 'db_creds.yaml']
        self.read_db_creds(yaml_files_list=yaml_files_list, verbose=verbose)

        # read database credentials
        self.init_db_engine(verbose=verbose)

        # list tables
        self.list_db_tables(verbose=verbose)


    def read_db_creds(self, yaml_files_list: list[str], verbose: Optional[bool] = False):
        """
        Read database credentials from a list of .yaml file
        """
        for yaml_file in yaml_files_list:

            # Define the path to your YAML file
            load_path = self.paths_dict['config'] / yaml_file

            # Load the YAML file
            try:
                # load yaml credentials, update the object
                with open(load_path , 'r') as file:
                    new_creds_dict = yaml.safe_load(file)

                if self.db_creds_dict is None:
                    self.db_creds_dict = new_creds_dict
                else:
                    (self.db_creds_dict).update(new_creds_dict)

            # handle errors
            except FileNotFoundError:
                logger.error(f"read_db_creds: The file {yaml_file} does not exist.")
            except yaml.YAMLError as exc:
                logger.error(f"read_db_creds: error while parsing {yaml_file} file - {exc}")

        # log credentials
        if verbose:
            logger.info("")
            logger.info("The following database credentials were succesfully loaded:")
            logger.info("")
            for key in self.db_creds_dict.keys():
                logger.info(f"    {key}:")
                logger.info(f"      {self.db_creds_dict[key]}")


    def init_db_engine(self, verbose: Optional[bool] = False):
        """
        Initialise and return an sqlalchemy database engine
        """
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = self.db_creds_dict['RDS_POSTGRES']
        DATABASE = 'Pagila'
        PORT = 5432

        # create sqlalchemy engine
        try:
            self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

            if verbose: 
                logger.info("")
                logger.info("Sqlalchemy engine was sucessfullt created.")

        except Exception as e:
            logger.error(f"init_db_engine: could not initiate the engine - {e}")


    def list_db_tables(self, verbose: Optional[bool] = False):
        """
        List database tables
        """

        try:
            inspector = inspect(self.engine)
            self.tables_list = inspector.get_table_names()

            if verbose: 
                logger.info("")
                logger.info("List of available database tables:")
                logger.info("")

                for table in self.tables_list:
                    logger.info(f"    {table},")
    
        except Exception as e:
            logger.error(f"list_db_tables: cound not fetch tables names - {e}")

    