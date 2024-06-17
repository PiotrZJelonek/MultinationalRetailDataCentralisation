# Main 'Multinational Retail Centralisation' project runner
from fire import Fire
from loguru import logger
from internal.main_helper import (
    setup,
    cleanup,
)
from classes.database_utils import DatabaseConnector
from classes.data_extraction import DataExtractor
from classes.data_cleaning import DataCleaning

def main():
    """
    Main 'Multinational Retail Centralisation' project runner
    `"""
    # define project name
    project_name = 'Multinational Retail Data Centralisation'

    # setup
    paths, start_time = setup(project_name=project_name)

    # instantiate the connector
    dc = DatabaseConnector(paths_dict=paths)

    # select table
    table_id = 7
    table_name = dc.tables_list[table_id]

    # instantiate data extractor
    de = DataExtractor(dc=dc) 

    # fetch a table
    df = de.read_rds_table(table_name=table_name)

    # log table name and head
    logger.info("")
    logger.info(f" table {table_id} - {table_name}")
    logger.info("")
    logger.info(print(df.head(5)))

    # cleanup
    cleanup(paths=paths, start_time=start_time, project_name=project_name)


if __name__ == "__main__":
    Fire(main)
