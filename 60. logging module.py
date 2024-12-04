# How do you log a simple informational message using thelogging module?

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(level=logging.INFO)
logging.info('This is an informational message')