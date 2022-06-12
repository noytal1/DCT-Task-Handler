import logging
from datetime import datetime

"""
    creating a logger for the task execution
"""

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y, %H-%M-%S")

logging.basicConfig(level=logging.INFO, filename='destination/logs/{}.log'.format(dt_string), filemode='w',
                    format='%(asctime)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger("DCT logger")
