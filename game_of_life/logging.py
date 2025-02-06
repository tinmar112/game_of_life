import argparse
import colorlog
import logging

def set_logger(logger: logging.Logger, args: argparse.Namespace) -> None:
    """Sets up a colorlog logger."""

    if args.verbose == 1:
        logger.setLevel(logging.INFO)
    elif args.verbose == 2:
        logger.setLevel(logging.DEBUG)
    
    color_fmt = colorlog.ColoredFormatter(
    "%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
    log_colors={
        "DEBUG": "yellow",
        "INFO": "green",
        "WARNING": "purple",
        "ERROR": "red",
        "CRITICAL": "red",
        })
    
    color_handler = colorlog.StreamHandler()
    color_handler.setFormatter(color_fmt)
    logger.addHandler(color_handler)