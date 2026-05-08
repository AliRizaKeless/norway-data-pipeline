import json
from datetime import datetime
from pathlib import Path

import pandas as pd

from src.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from src.logger import get_logger

logger = get_logger()

def get_latest_raw_file() -> Path:
    """
    Get the most recent raw JSON file from the raw data directory.
    """
    json_files = sorted(RAW_DATA_DIR.glob("ssb_raw_*.json"), reverse=True)

    if not json_files:
        raise FileNotFoundError("No raw JSON files found in data/raw.")

    return json_files[0]


def load_raw_data(file_path: Path) -> dict:
    """
    Load raw JSON data from file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def transform_to_dataframe(raw_data: dict) -> pd.DataFrame:
    """
    Transform SSB JSON-stat response into a pandas DataFrame.
    """
    dimensions = raw_data.get("dimension", {})
    values = raw_data.get("value", [])
    dimension_ids = raw_data.get("id", [])
    sizes = raw_data.get("size", [])

    if not dimensions or not values or not dimension_ids or not sizes:
        raise ValueError("Raw SSB data does not contain valid JSON-stat fields.")

    records = []

    vare_dimension = dimensions.get("VareTjenesteGrp", {})
    time_dimension = dimensions.get("Tid", {})

    vare_categories = vare_dimension.get("category", {}).get("label", {})
    time_categories = time_dimension.get("category", {}).get("label", {})

    vare_codes = list(vare_categories.keys())
    time_codes = list(time_categories.keys())

    for vare_index, vare_code in enumerate(vare_codes):
        for time_index, time_code in enumerate(time_codes):
            value_index = vare_index * len(time_codes) + time_index

            if value_index >= len(values):
                continue

            records.append(
                {
                    "commodity_group_code": vare_code,
                    "commodity_group": vare_categories.get(vare_code),
                    "period": time_code,
                    "period_label": time_categories.get(time_code),
                    "cpi_index": values[value_index],
                    "source": raw_data.get("source"),
                    "updated": raw_data.get("updated"),
                }
            )

    df = pd.DataFrame(records)

    if df.empty:
        raise ValueError("Transformation produced an empty DataFrame.")

    return df


def save_processed_data(df: pd.DataFrame) -> Path:
    """
    Save transformed data as a timestamped CSV file.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = PROCESSED_DATA_DIR / f"ssb_processed_{timestamp}.csv"

    df.to_csv(output_file, index=False)

    logger.info(f"Processed data saved: {output_file}")
    return output_file


def run_transformation(raw_file_path: Path | None = None) -> Path:
    """
    Run transformation step and return processed file path.
    """
    if raw_file_path is None:
        raw_file_path = get_latest_raw_file()

    raw_data = load_raw_data(raw_file_path)
    df = transform_to_dataframe(raw_data)
    processed_file_path = save_processed_data(df)

    return processed_file_path