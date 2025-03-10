import logging

logger = logging.getLogger("dev")


def init_logging():
    console_format = "%(name)s | %(levelname)s | %(module)s | %(filename)s | %(funcName)s | %(lineno)d | %(message)s"
    console_logging_level = logging.DEBUG

    file_format = "%(asctime)s | %(name)s | %(levelname)s | %(module)s | %(filename)s | %(funcName)s | %(lineno)d | %(message)s"
    file_logging_level = logging.DEBUG
    file_name = "app.log"
    encoding = "utf-8"
    mode = "a"

    # set console
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(console_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    logger.setLevel(console_logging_level)

    # # set file
    file_handler = logging.FileHandler("app.log", mode=mode, encoding=encoding)
    file_formatter = logging.Formatter(file_format)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    file_handler.setLevel(file_logging_level)

    logger.info("Start logging")


# initialisation
init_logging()

# use
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
