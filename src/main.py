# -*- coding: utf-8 -*-
"""
a doc string
"""
from devsetgo_lib.file_functions import create_sample_files
from src.com_lib.log_config import config_log
from loguru import logger

# initiate logging
config_log()


def main(file_name: str, sample_size: int):
    # start something like test files :-)
    create_sample_files(file_name, sample_size=100)
    logger.info(f"Files named {file_name} create with sample size of {sample_size}")
    return "complete"


if __name__ == "__main__":
    # start the main process
    main("test_file", 100)
