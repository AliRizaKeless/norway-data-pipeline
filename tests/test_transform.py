import pandas as pd

from src.transform import transform_to_dataframe


def test_transform_to_dataframe_returns_dataframe():
    sample_raw_data = {
        "source": "Statistics Norway",
        "updated": "2026-05-08",
        "dimension": {
            "VareTjenesteGrp": {
                "category": {
                    "label": {
                        "01": "Food",
                    }
                }
            },
            "Tid": {
                "category": {
                    "label": {
                        "2026M01": "January 2026",
                    }
                }
            },
        },
        "id": ["VareTjenesteGrp", "Tid"],
        "size": [1, 1],
        "value": [123.4],
    }

    df = transform_to_dataframe(sample_raw_data)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    expected_columns = [
        "commodity_group_code",
        "commodity_group",
        "period",
        "period_label",
        "cpi_index",
        "source",
        "updated",
    ]

    for column in expected_columns:
        assert column in df.columns

import pytest


def test_transform_raises_error_for_invalid_data():
    invalid_data = {}

    with pytest.raises(ValueError):
        transform_to_dataframe(invalid_data)