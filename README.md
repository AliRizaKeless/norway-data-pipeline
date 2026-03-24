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
