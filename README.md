# norway-data-pipeline

End-to-end data pipeline using Norwegian public data (SSB), built with Python and integrated with Azure Blob Storage.

## Project Overview

This project fetches data from Statistics Norway (SSB), stores the raw data locally, transforms it into a processed format, and uploads the result to Azure Blob Storage.

The pipeline is designed to demonstrate core data engineering skills:
- API data ingestion
- local raw data storage
- data transformation
- cloud upload to Azure
- fallback handling when external API access fails

## Tech Stack

- Python
- Pandas
- REST API (SSB)
- Azure Blob Storage
- dotenv

## Architecture

```text
SSB API
   ↓
Python Pipeline
   ↓
Raw JSON Storage
   ↓
Data Transformation (pandas)
   ↓
Processed Output (CSV)
   ↓
Azure Blob Storage  

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
python src/transform_data.py
python src/upload_to_azure.py

Environment Variables

Create a .env file in the project root and add:

AZURE_CONNECTION_STRING=your_connection_string_here

Current Features
Fetches data from the SSB API
Stores raw JSON locally
Transforms JSON into CSV
Uploads processed data to Azure Blob Storage
Supports fallback local data if API access fails

Project Structure
norway-data-pipeline/
├── data/
├── output/
├── src/
│   ├── main.py
│   ├── transform_data.py
│   └── upload_to_azure.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

Next Steps
Add Terraform for Azure infrastructure
Add better logging
Add automated pipeline execution
Improve error handling

