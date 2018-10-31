import logging
import logging.config

logging.config.fileConfig("logger.ini")
logger = logging.getLogger("root")

