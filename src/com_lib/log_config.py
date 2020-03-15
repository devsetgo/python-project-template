# -*- coding: utf-8 -*-
from pathlib import Path
import logging
import sys
from loguru import logger
from settings import LOGURU_RETENTION, LOGURU_ROTATION


def config_log():
    log_path = Path.cwd().joinpath("log").joinpath("app_log.log")
    logger.add(
        log_path,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        enqueue=True,
        backtrace=False,
        rotation=LOGURU_ROTATION,
        retention=LOGURU_RETENTION,
        compression="zip",
    )
    logger.add(sys.stderr, format="{level} | {message} ",
                level="INFO", colorize=True, enqueue=True, backtrace=True)
