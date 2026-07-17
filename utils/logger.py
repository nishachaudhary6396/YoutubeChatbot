"""
logger.py

Configures logging for the entire application.
"""

import logging
from pathlib import Path

# Create the logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

LOG_FILE = "logs/application.log"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def get_logger(module_name: str) -> logging.Logger:
    """
    Returns a logger for the specified module.
    """
    return logging.getLogger(module_name)