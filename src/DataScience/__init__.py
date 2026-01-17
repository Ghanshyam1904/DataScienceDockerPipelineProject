import os
import sys
import logging

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "logging.log")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")
