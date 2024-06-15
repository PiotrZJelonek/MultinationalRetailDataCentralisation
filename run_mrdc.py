# Main 'Multinational Retail Centralisation' project runner
from fire import Fire
from internal.main_helper import (
    setup,
    cleanup,
)

import numpy as np
import pandas as pd
import os
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

    # process
    # ...

    print('hello word!')

    # cleanup
    cleanup(paths=paths, start_time=start_time, project_name=project_name)


if __name__ == "__main__":
    Fire(main)
