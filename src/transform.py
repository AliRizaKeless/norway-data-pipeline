import json
import os
from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")


def get_latest_json_file():
    json_files = sorted(DATA_DIR.glob("data_*.json"), reverse=True)
    if not json_files:
        raise FileNotFoundError("No JSON data files found in the data folder.")
    return json_files[0]


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def transform_to_dataframe(raw_data):
    df = pd.json_normalize(raw_data)
    return df


def save_output(df):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = OUTPUT_DIR / "ssb_data_flattened.csv"
    df.to_csv(output_file, index=False)
    print(f"Transformed data saved to: {output_file}")


def main():
    latest_file = get_latest_json_file()
    raw_data = load_json(latest_file)
    df = transform_to_dataframe(raw_data)
    save_output(df)


if __name__ == "__main__":
    main()
