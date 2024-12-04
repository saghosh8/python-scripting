# How do you congurethe logging to log messages with severity level WARNING and above?

import logging

logging.basicConfig(level=logging.WARNING)
logging.warning("This is Warning Message")
logging.error("This is Error Message")
logging.critical("This is Critical Message")

