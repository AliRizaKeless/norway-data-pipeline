import json
from upload_to_azure import upload_file
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Fetch data from API or fallback source
def fetch_data():
    sample_data = {
        "source": "SSB demo fallback",
        "generated_at": datetime.now().isoformat(),
        "data": [
            {"year": 2023, "value": 100},
            {"year": 2024, "value": 120},
            {"year": 2025, "value": 135}
        ]
    }
    return sample_data

def save_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = DATA_DIR / f"data_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {file_path}")
    return file_path

def main():
    print("Starting pipeline...")

    data = fetch_data()
    file_path = save_data(data)

    upload_file(file_path)

    print("Pipeline finished successfully")

if __name__ == "__main__":
    main()