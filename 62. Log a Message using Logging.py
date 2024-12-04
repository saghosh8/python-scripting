# How do you log a message to a file using the logging module with timestramp?

import logging

logging.basicConfig(filename = 'app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('This message will be logged to a file.')