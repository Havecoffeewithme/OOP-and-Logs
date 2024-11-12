import logging


logger = logging.getLogger()
logger = logging.Logger("MYLOGGER")

logger.info("Logger successfully created")
logger.log(logging.INFO, "successful")

logger.critical("critical message")
logger.log(logging.CRITICAL, "critical!")

# removing the handlers from default root looger

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.INFO)
