import logging

logger = logging.getLogger("Scrapper")
formatter = logging.Formatter(
    "%(levelname)s %(asctime)s: %(message)s", datefmt="%H:%M:%S"
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

if logger.hasHandlers():
    logger.handlers.clear()

logger.addHandler(handler)
logger.propagate = False
logger.setLevel(logging.INFO)