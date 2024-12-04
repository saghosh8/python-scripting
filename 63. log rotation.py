# How do you implement log rotation in Python?

import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=3)

logging.basicConfig(handlers=[handler], level=logging.DEBUG)