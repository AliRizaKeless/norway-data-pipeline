Norway Data Pipeline

A production-style ETL pipeline that ingests real public data from Statistics Norway (SSB), transforms JSON-stat datasets into analytics-ready CSV files, validates data quality, and uploads processed outputs to Azure Blob Storage.

Architecture
SSB API
   ↓
Raw JSON ingestion
   ↓
Data transformation with pandas
   ↓
Data quality validation
   ↓
Processed CSV generation
   ↓
Azure Blob Storage upload

Features
- Real-time ingestion from the Statistics Norway API
- Modular ETL pipeline architecture
- JSON-stat to tabular transformation
- Structured logging and exception handling
- Retry logic for resilient API ingestion
- Data quality validation checks
- Azure Blob Storage integration
- Terraform infrastructure provisioning
- Automated testing with pytest
- GitHub Actions CI workflow
- Docker-ready project structure

Tech Stack
- Python
- pandas
- Azure Blob Storage
- Terraform
- GitHub Actions
- pytest
- Docker
- tenacity
- requests

Project Structure
norway-data-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
├── infra/
├── src/
├── tests/
│
├── Dockerfile
├── requirements.txt
└── README.md

Running the Pipeline

Install dependencies:
pip install -r requirements.txt

Run the ETL pipeline:
python -m src.pipeline

Run tests:
python -m pytest

Infrastructure
Terraform is used to provision:
- Azure Resource Group
- Azure Storage Account
- Azure Blob Container

Terraform files are located in:
infra/

CI/CD
GitHub Actions automatically runs tests on:
- Push
- Pull requests

Workflow configuration:
.github/workflows/ci.yml

Example Output
Processed datasets are saved as timestamped CSV files:
data/processed/ssb_processed_20260509_124720.csv

Raw API snapshots are stored as JSON:
data/raw/ssb_raw_20260509_124720.json

Future Improvements
- Scheduled pipeline execution
- Data warehouse integration
- Dashboarding and visualization
- Monitoring and alerting
- Container deployment

Author
Ali Riza Keless