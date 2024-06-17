import os
from pathlib import Path
from typing import Tuple

from loguru import logger
from time import time

def setup(project_name: str) -> Tuple[dict, float]:
    """
    Create paths for the experiment. Start the clock.
    """
    path = Path(os.getcwd()) # os.pardir

    # define paths
    paths = dict()
    paths["log"] = path / "log"
    paths["config"] = path / "config"
    paths["classes"] = path / "classes"
    paths["internal"] = path / "internal"
    paths["input"] = path / "input"
    paths["output"] = path / "output"

    # process project name
    project_snake_case = project_name.lower().replace(" ", "_")
    project_display = project_name.upper().replace("_", " ")

    # creating new log
    # logger.remove()
    log_str = f"run_{project_snake_case}" + "_{time}.log"
    logger.add(paths["log"] / log_str)

    # output
    logger.info("")
    logger.info(f"-------------------------------------- {project_display} RUN -------------------------------------- ")
    logger.info("")

    # log paths
    logger.info("All the defined paths:")
    for key in paths.keys():
        logger.info(f"    {key}:")
        logger.info(f"      {paths[key]}")

    # create paths if they do not exist
    for key, path in paths.items():
        if not os.path.exists(path):
            os.makedirs(path)
    logger.info("")
    logger.info("If any paths were missing, they were automatically created.")

    # start the clock
    start_time = time()

    return paths, start_time

def cleanup(paths: dict, start_time: float, project_name: str) -> None:
    """
    Log execution time. Clean logs.

    """
    # log execution time
    es = round(time() - start_time)
    logger.info("")
    logger.info(f"Total {project_name} runtime: {es:.2f} seconds.")

    # clean logs
    # clean_logs(paths)
