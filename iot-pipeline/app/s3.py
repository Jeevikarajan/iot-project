import boto3
import json
import os
from dotenv import load_dotenv
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("BUCKET_NAME")

def upload_stats_to_s3(data):
    try:
        filename = f"analytics/{datetime.utcnow().isoformat()}.json"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=json.dumps(data),
            ContentType="application/json"
        )

        return filename
    except Exception as e:
        import traceback
        print("S3 ERROR FULL:")
        traceback.print_exc()
        return None