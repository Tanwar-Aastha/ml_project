import logging
import os
from datetime import datetime


# creating the log_file format
LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"

# Creating the log path by joining the current working directory with the log_path
log_path = os.path.join(os.getcwd(), LOG_FILE)

# creating the directory
os.mkdir(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

