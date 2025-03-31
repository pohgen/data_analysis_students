import os

from dotenv import load_dotenv
from google.cloud import bigquery
from google.oauth2 import service_account


load_dotenv()


def create_bq_client():
    CREDENTIALS = os.getenv("CREDENTIALS")
    PROJECT_ID = os.getenv("PROJECT_ID")

    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS
    )

    client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
    return client
