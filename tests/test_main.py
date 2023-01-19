import pandas as pd
import pytest

from app.main import DATA_DICT, NEW_COLUMN, NEW_DATA, Data


def test_init_df() -> None:
    """Test dataframe initiation."""
    data = Data(DATA_DICT)
    assert data.df is not None, "dataframe not initiated"


def test_init_columns() -> None:
    """Test dataframe dimensions."""
    data = Data(DATA_DICT)
    assert len(data.columns) == 3, "incorrect dataframe dimensions"


def test_add_dataframe_column() -> None:
    """Test that a new dataframe column was added."""
    data = Data(DATA_DICT)
    data.add_dataframe_column(NEW_COLUMN)
    assert (
        NEW_COLUMN not in data.columns or len(data.columns) != 4
    ), "dataframe column does not exist"


def test_add_dataframe_column_vals() -> None:
    """Test that a column was filled with NaN."""
    data = Data(DATA_DICT)
    data.add_dataframe_column(NEW_COLUMN)
    for idx, row in enumerate(data.df[NEW_COLUMN]):
        assert pd.isna(
            data.df.iloc[idx, 3],
        ), f"column initiated with value other than NaN {row}"


def test_fill_dataframe_column() -> None:
    """Check that a column was filled with correct values."""
    data = Data(DATA_DICT)
    data.add_dataframe_column(NEW_COLUMN)
    data.fill_dataframe_column(NEW_COLUMN, NEW_DATA)
    for idx, row in enumerate(data.df[NEW_COLUMN]):
        assert row == NEW_DATA[idx], "column contains incorrect fill values"


if __name__ == "__main__":
    pytest.main()
