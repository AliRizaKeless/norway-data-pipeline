import requests
import json
import os
from datetime import datetime

API_URL = "https://api.statbank.ssb.no:443/statbank/sq/10070628/"


def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def save_data(data):
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"data/data_{timestamp}.json"

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Data saved: {file_name}")


def main():
    data = fetch_data()
    save_data(data)


if __name__ == "__main__":
    main()
