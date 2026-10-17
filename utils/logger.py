import logging
from pathlib import Path
from datetime import datetime

def get_logger(name: str = "TestLogger") -> logging.Logger:
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if logger is already configured
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)

    # Log file name with current date
    log_file = log_dir / f"execution_{datetime.now().strftime('%Y-%m-%d')}.log"

    # Formatter: Timestamp | Log Level | Logger Name | Message
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console Handler (Terminal output)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger