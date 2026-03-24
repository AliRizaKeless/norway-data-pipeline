import requests
import json
from datetime import datetime

API_URL = "https://api.statbank.ssb.no:443/statbank/sq/10070628/"


def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def save_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"data_{timestamp}.json"

    with open(file_name, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Data saved: {file_name}")


def main():
    data = fetch_data()
    save_data(data)


if __name__ == "__main__":
    main()
