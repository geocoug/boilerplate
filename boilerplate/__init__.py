#!/usr/bin/env python

from ._version import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)
from .api import app
from .boilerplate import Boilerplate

__all__ = [
    "Boilerplate",
    "app",
    "__version__",
    "__description__",
    "__title__",
    "__author__",
    "__author_email__",
    "__license__",
    "__url__",
]
