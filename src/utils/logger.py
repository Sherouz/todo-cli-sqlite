# src/utils/logger.py

from pathlib import Path
import logging
import sys

# Log directory path
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.parent.mkdir(exist_ok=True, parents=True)


def setup_logger(
    name: str = "Todo CLI",
    logfile: str | None = None,
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG
) -> logging.Logger:
    """
    Configure and return a logger.
    - console: INFO
    - file: DEBUG
    """
    
    if logfile is None:
        logfile = str(LOG_DIR / "app.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # base level to capture everything

    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatter
    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d | %H:%M:%S"
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(console_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # file handler (ensure path exists)
    log_path = Path(logfile)
    log_path.parent.mkdir(exist_ok=True, parents=True)

    fh = logging.FileHandler(logfile, encoding="utf-8")
    fh.setLevel(file_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # return the configured Logger
    return logger


# ready-to-use logger
log = setup_logger()