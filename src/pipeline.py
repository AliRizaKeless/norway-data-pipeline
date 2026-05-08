from src.ingest import run_ingestion
from src.transform import run_transformation
from src.upload import run_upload


def run_pipeline() -> None:
    """
    Run the full ETL pipeline:
    1. Ingest raw data
    2. Transform raw data into processed CSV
    3. Upload processed CSV to Azure Blob Storage
    """
    print("Starting Norway data pipeline...")

    raw_file_path = run_ingestion()
    processed_file_path = run_transformation(raw_file_path)
    run_upload(processed_file_path)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()