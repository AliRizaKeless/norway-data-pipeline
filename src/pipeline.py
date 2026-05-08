from src.ingest import run_ingestion
from src.logger import get_logger
from src.transform import run_transformation
from src.upload import run_upload

logger = get_logger()


def run_pipeline() -> None:
    """
    Run the full ETL pipeline.
    """

    try:
        logger.info("Starting Norway data pipeline")

        raw_file_path = run_ingestion()

        logger.info(f"Raw data file created: {raw_file_path}")

        processed_file_path = run_transformation(raw_file_path)

        logger.info(f"Processed file created: {processed_file_path}")

        run_upload(processed_file_path)

        logger.info("Upload step completed")

        logger.info("Pipeline completed successfully")

    except Exception as error:
        logger.exception(f"Pipeline failed: {error}")
        raise


if __name__ == "__main__":
    run_pipeline()