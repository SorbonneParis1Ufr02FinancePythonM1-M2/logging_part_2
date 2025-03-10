import logging

# parameters
level = logging.DEBUG
format = "%(asctime)s | %(name)s | %(levelname)s | %(module)s | %(filename)s | %(funcName)s | %(lineno)d | %(message)s"

# setting
logging.basicConfig(level=level, format=format)

# initialisation
logger = logging.getLogger("dev")

# use
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
