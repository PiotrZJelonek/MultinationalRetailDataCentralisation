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
    Main 'Multinational Retail Centralisation' project runner'
    """
    # define project name
    project_name = 'Multinational Retail Data Centralisation'

    # setup
    paths, start_time = setup(project_name=project_name)

    # instantiate the connector
    aws = DatabaseConnector(paths_dict=paths)

    # setup the engine
    aws.init_db_engine(yaml_file='aws_creds.yaml', verbose=True)

    # list tables
    aws.list_db_tables(verbose=True)

    # instantiate data extractor
    de = DataExtractor(dc=aws) 

    # select table
    table_id = 2
    table_name = aws.tables_list[table_id]

    # fetch a table
    df = de.read_aws_table(table_name=table_name)

    # log table name and head
    logger.info("")
    logger.info(f"Loading table {table_id}: {table_name}")
    logger.info("")

    # clean data frame
    if 'index' in df.columns:
        df.drop(columns={'index'}, inplace=True)
        df.reset_index

    # save data frame to csv
    file_csv = "users_df.csv"
    df.to_csv(paths["output"] / file_csv, index=False)

#     print(df)

#     # cleaning?

#     table_name = 'dim_users'
#     dc.upload_to_db(df=df, table_name=table_name, verbose=True)


# placeholders
    # # instantiate data cleaning
    # dc = DataCleaning(df=df)
    # # clean data
    # df = dc.clean_user_data()
    # df = dc.clean_movie_data(df=df)


    # cleanup
    cleanup(paths=paths, start_time=start_time, project_name=project_name)


if __name__ == "__main__":
    Fire(main)
