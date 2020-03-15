# -*- coding: utf-8 -*-
"""
a doc string
"""
from devsetgo_lib.file_functions import create_sample_files


def main(file_name: str):
    # start something like test files :-)
    create_sample_files(file_name, sample_size=100)
    return "complete"


if __name__ == "__main__":
    # start the main process
    main("test_file")
