import os
import time

from dotenv import load_dotenv
from google.cloud import bigquery

from big_query_connection import create_bq_client

load_dotenv()
client = create_bq_client()
project_id = os.getenv("PROJECT_ID")

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True
)

dataset_id = project_id + "." + "student_performance" + "."

files = [
    ("parsed_csv/Students_Home_Info_Dataset.csv", f"{dataset_id}students_home_info"),
    ("parsed_csv/Students_Parents_Info_Dataset.csv", f"{dataset_id}parents_info"),
    ("parsed_csv/Students_Personal_info_Dataset.csv", f"{dataset_id}students_personal_info"),
    ("parsed_csv/Students_Univercity_Dataset.csv", f"{dataset_id}students_university"),
]

for file_open, table_id in files:
    print(f"Uploading {file_open} in the {table_id}")

    with open(file_open, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    while job.state != "DONE":
        time.sleep(2)
        job.reload()
        print(job.state)
