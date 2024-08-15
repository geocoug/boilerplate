#!/usr/bin/env python

from __future__ import annotations

import argparse
import logging
import sys
import traceback

from ._version import __description__, __version__

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.NullHandler()],
)
logger = logging.getLogger(__name__)


class Boilerplate:
    def __init__(self: Boilerplate, x: float, y: float) -> None:
        """A simple class to perform basic arithmetic operations.

        Args:
            x (float): The first number.
            y (float): The second number.
        """
        self.x = x
        self.y = y

    def add(self: Boilerplate) -> float:
        """Add two numbers together."""
        return self.x + self.y

    def subtract(self: Boilerplate) -> float:
        """Subtract two numbers."""
        return self.x - self.y

    def multiply(self: Boilerplate) -> float:
        """Multiply two numbers."""
        return self.x * self.y

    def divide(self: Boilerplate) -> float | str:
        """Divide two numbers."""
        if self.y == 0:
            return "Cannot divide by zero."
        return self.x / self.y

    def __repr__(self: Boilerplate) -> str:
        """Return the class representation."""
        return f"Boilerplate(x={self.x}, y={self.y})"


def clparser() -> argparse.Namespace:
    """Command line argument parser for Boilerplate."""
    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="enable debug mode.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose mode.",
    )
    parser.add_argument("x", type=float, help="The first number.")
    parser.add_argument("y", type=float, help="The second number.")
    return parser.parse_args()


def cli() -> None:
    """Command line interface for Boilerplate."""
    args = clparser()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s %(name)s (%(lineno)d) %(levelname)s: %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]",
        )
        for handler in logger.handlers:
            handler.setFormatter(formatter)
    if args.verbose:
        logger.addHandler(logging.StreamHandler(sys.stdout))
    try:
        boilerplate = Boilerplate(args.x, args.y)
        logger.info(boilerplate)
        logger.info(f"Add: {boilerplate.add()}")
        logger.info(f"Subtract: {boilerplate.subtract()}")
        logger.info(f"Multiply: {boilerplate.multiply()}")
        logger.info(f"Divide: {boilerplate.divide()}")
    except SystemExit as x:
        sys.exit(x.code)
    except ValueError:
        strace = traceback.extract_tb(sys.exc_info()[2])[-1:]
        lno = strace[0][1]
        src = strace[0][3]
        logger.error(
            f"ValueError on line {lno}: {sys.exc_info()[1]}",
        )
        sys.exit(1)
    except Exception:
        strace = traceback.extract_tb(sys.exc_info()[2])[-1:]
        lno = strace[0][1]
        src = strace[0][3]
        logger.error(
            f"Uncaught exception {sys.exc_info()[0]!s} ({sys.exc_info()[1]}) on line {lno} ({src}).",
        )
        sys.exit(1)


if __name__ == "__main__":
    cli()
