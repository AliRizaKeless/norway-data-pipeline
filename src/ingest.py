import json
from datetime import datetime
from pathlib import Path
import requests

from tenacity import retry, stop_after_attempt, wait_exponential
from src.config import RAW_DATA_DIR, SSB_API_URL
from src.logger import get_logger

logger = get_logger()

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
)
def fetch_data() -> dict:
    """
    Fetch CPI data from Statistics Norway API.
    """
    params = {
        "valuecodes[Tid]": "top(3)",
        "valuecodes[VareTjenesteGrp]": "??",
        "valuecodes[ContentsCode]": "KpiIndMnd",
    }

    response = requests.get(SSB_API_URL, params=params, timeout=30)
    response.raise_for_status()

    return response.json()


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