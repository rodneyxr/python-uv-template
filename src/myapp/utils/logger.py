import logging


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a logger with the specified name and level.

    Parameters:
    name (str): The name of the logger.
    level (logging.Level, optional): The level of the logger. Defaults to logging.INFO.

    Returns:
    logging.Logger: The logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure the logger has at least one handler
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(module)s:%(lineno)d | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
