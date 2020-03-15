# -*- coding: utf-8 -*-
import datetime
import unittest
import tempfile
import pytest
from src.main import main

time_str = datetime.datetime.now()


class Test(unittest.TestCase):
    def test_main(self):

        file_name = "test_test"
        sample_size = 100
        result = main(file_name=file_name, sample_size=sample_size)
        assert result == "complete"
