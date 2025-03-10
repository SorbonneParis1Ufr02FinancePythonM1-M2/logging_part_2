import logging
import os
from logging import config

from helpers_serialize import get_serialized_data
from typing import Final



def init_logger_from_file(logger_name: str, config_full_path: str) -> logging.Logger:
    """
    Initializes the logger and run the log application if needed

    :param logger_name:
    :param config_full_path:
    :return: logger
    :rtype: logging.Logger
    """
    dict_config = get_serialized_data(full_path=config_full_path)
    log_file_path = dict_config.get("handlers").get("file").get("filename")
    config.dictConfig(dict_config)
    logger = logging.getLogger(logger_name)
    logger.info(f"start logger {logger_name}")
    logger.info(f"logger filename={log_file_path}")

    if dict_config.get("open_logging_file") and log_file_path:
        os.startfile(log_file_path)

    return logger


LOGGER_NAME: Final[str] = "development_sorbonne"
LOGGING_CONFIG_FILE: Final[str] = r"config_logging.yaml"

logging_config_full_path = os.path.join(os.path.dirname(__file__), LOGGING_CONFIG_FILE)
logger = init_logger_from_file(
    logger_name=LOGGER_NAME, config_full_path=logging_config_full_path
)

# use
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")