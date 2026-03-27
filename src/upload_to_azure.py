import os
from pathlib import Path

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "data"


def get_latest_file():
    files = sorted(Path("data").glob("data_*.json"), reverse=True)
    if not files:
        raise FileNotFoundError("No files found in data folder")
    return files[0]


def upload_file(file_path):
    if not CONNECTION_STRING:
        raise ValueError("AZURE_CONNECTION_STRING is not set in the .env file")

    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=file_path.name
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"Uploaded {file_path.name} to Azure Blob Storage")


def main():
    file_path = get_latest_file()
    upload_file(file_path)


if __name__ == "__main__":
    main()
