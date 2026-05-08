import json
from datetime import datetime
from pathlib import Path

import pandas as pd

from src.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


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
    Transform raw JSON data into a pandas DataFrame.
    """
    records = raw_data.get("data", [])

    if not records:
        raise ValueError("Raw data does not contain a valid 'data' field.")

    df = pd.DataFrame(records)

    df["source"] = raw_data.get("source")
    df["generated_at"] = raw_data.get("generated_at")

    return df


def save_processed_data(df: pd.DataFrame) -> Path:
    """
    Save transformed data as a timestamped CSV file.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = PROCESSED_DATA_DIR / f"ssb_processed_{timestamp}.csv"

    df.to_csv(output_file, index=False)

    print(f"Processed data saved: {output_file}")
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