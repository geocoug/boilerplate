#!/usr/bin/env python
import logging
import os
from datetime import datetime

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console log handler
logger.addHandler(logging.StreamHandler())

# Log file handler
if not os.path.exists("logs"):
    os.mkdir("logs")
logfile = os.path.join("logs", f"log_{datetime.now().strftime('%Y%m%d_%H%M')}.log")
formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
fh = logging.FileHandler(logfile)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)


data_dict = {
    "col1": [1, 2, 3, 4, 5],
    "col2": ["a", "b", "c", "d", "e"],
    "col3": [True, True, False, True, True],
}

NEW_COLUMN = "new_col"
new_data = ["z", "y", "x", "w", "v"]


class Data:
    """Data class."""

    def __init__(self, data: dict) -> None:
        self.df = pd.DataFrame(data)
        self.columns = list(self.df.columns)

    def add_dataframe_column(self, col_name: str) -> None:
        """Add a new dataframe column."""
        self.df[col_name] = np.nan

    def fill_dataframe_column(self, col_name: str, data: list) -> None:
        """Fill an empty dataframe column."""
        self.df[col_name] = data


if __name__ == "__main__":
    dtable = Data(data_dict)
    dtable.add_dataframe_column(NEW_COLUMN)
    dtable.fill_dataframe_column(NEW_COLUMN, new_data)
    logger.info(dtable.columns)
    logger.info(dtable.df)
