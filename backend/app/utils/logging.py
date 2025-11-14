import logging
from typing import Any

_LOGGER_NAME = "osint_shield"


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a namespaced logger configured for structured console output."""

    logger_name = f"{_LOGGER_NAME}.{name}" if name else _LOGGER_NAME
    logger = logging.getLogger(logger_name)
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s :: %(message)s",
        )
    return logger
