import pandas as pd


REQUIRED_COLUMNS = [
    "commodity_group_code",
    "commodity_group",
    "period",
    "period_label",
    "cpi_index",
    "source",
    "updated",
]


def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate transformed DataFrame before saving.
    """
    if df.empty:
        raise ValueError("Data quality check failed: DataFrame is empty.")

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(
            f"Data quality check failed: Missing columns: {missing_columns}"
        )

    if df["cpi_index"].isnull().any():
        raise ValueError("Data quality check failed: cpi_index contains null values.")

    if not pd.api.types.is_numeric_dtype(df["cpi_index"]):
        raise ValueError("Data quality check failed: cpi_index must be numeric.")