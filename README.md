# norway-data-pipeline

End-to-end data pipeline using Norwegian public data (SSB), built with Python and deployed to Azure using Terraform.

## Current Features
- Fetches data from the SSB API
- Stores raw JSON files in the `data/` folder
- Transforms raw JSON into flat CSV output using pandas
- Organizes raw and transformed data into separate folders

## Project Structure

```bash
norway-data-pipeline/
├── data/
├── output/
├── src/
│   ├── main.py
│   └── transform_data.py
├── requirements.txt
└── README.md

## Environment Variables

Create a `.env` file in the project root and add:

```env
AZURE_CONNECTION_STRING=your_connection_string_here

## Tech Stack

- Python
- Azure Blob Storage
- Pandas
- REST API (SSB)
- dotenv

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
python src/transform_data.py
python src/upload_to_azure.py
