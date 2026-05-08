from pathlib import Path

from azure.storage.blob import BlobServiceClient

from src.config import (
    AZURE_CONNECTION_STRING,
    AZURE_CONTAINER_NAME,
)

from src.logger import get_logger

logger = get_logger()

def upload_file(file_path: Path) -> None:
    """
    Upload a file to Azure Blob Storage.
    """

    if not AZURE_CONNECTION_STRING:
        raise ValueError(
            "AZURE_STORAGE_CONNECTION_STRING is not set in the .env file."
        )

    if not AZURE_CONTAINER_NAME:
        raise ValueError(
            "AZURE_CONTAINER_NAME is not set in the .env file."
        )

    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_CONNECTION_STRING
    )

    blob_client = blob_service_client.get_blob_client(
        container=AZURE_CONTAINER_NAME,
        blob=file_path.name,
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    logger.info(f"Uploaded file to Azure Blob Storage: {file_path.name}")


def run_upload(file_path: Path) -> None:
    """
    Run upload step.
    """
    upload_file(file_path)