import json
from datetime import datetime
from pathlib import Path

from src.config import RAW_DATA_DIR
from src.logger import get_logger

logger = get_logger()

def fetch_data():
    """
    Fetch data from Statistics Norway API.

    Currently returns fallback sample data.
    Real API integration will be added in the next step.
    """
    sample_data = {
        "source": "SSB demo fallback",
        "generated_at": datetime.now().isoformat(),
        "data": [
            {"year": 2023, "value": 100},
            {"year": 2024, "value": 120},
            {"year": 2025, "value": 135},
        ],
    }
    return sample_data


def save_raw_data(data: dict) -> Path:
    """
    Save raw API response as a timestamped JSON file.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DATA_DIR / f"ssb_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    logger.info(f"Raw data saved: {file_path}")
    return file_path


def run_ingestion() -> Path:
    """
    Run ingestion step and return saved raw file path.
    """
    data = fetch_data()
    raw_file_path = save_raw_data(data)
    return raw_file_path