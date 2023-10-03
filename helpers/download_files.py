import io
import os
import requests
import pandas as pd
from google.cloud import storage

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# services = ['fhv','green','yellow']
init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "de-zoomcamp-dtl-test")


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"

        # download it using requests via a pandas df
        request_url = f"{init_url}{service}/{file_name}"
        r = requests.get(request_url)
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        # dtypes and date columns
        set_dtypes = {"VendorID": "Int64",
                    "passenger_count": "Int64",
                    "store_and_fwd_flag": "object",
                    "PULocationID": "Int64",
                    "DOLocationID": "Int64",
                    "PUlocationID": "Int64",
                    "DOlocationID": "Int64",
                    "payment_type": "Int64",
                    "trip_type": "Int64",
                    "RatecodeID": "Int64"}

        # read it back into a parquet file
        df = pd.read_csv(file_name, compression='gzip', dtype=set_dtypes)

        # cast to date dtype
        date_cols_green = ["lpep_pickup_datetime", "lpep_pickup_datetime"]
        date_cols_yellow = ["tpep_pickup_datetime", "tpep_pickup_datetime"]
        date_cols_fhv = ["pickup_datetime", "dropOff_datetime"]
        
        date_col_parse = date_cols_green
        if service == "yellow":
            date_col_parse = date_cols_yellow
        elif service == "fhv":
            date_col_parse = date_cols_fhv
        
        df[date_col_parse[0]] = pd.to_datetime(df[date_col_parse[0]])
        df[date_col_parse[1]] = pd.to_datetime(df[date_col_parse[1]])
        
        # continue to parquet
        file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(file_name, engine='pyarrow')
        print(f"Parquet: {file_name}")

        # upload it to gcs 
        upload_to_gcs(BUCKET, f"data/{service}/{file_name}", file_name)
        print(f"GCS: data/{service}/{file_name}")


for taxi_type in ['yellow', 'green']:
    for year in ['2019', '2020']:
        web_to_gcs(year, taxi_type)
