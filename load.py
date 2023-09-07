import os
from utils import BucketAdapter

job_id = os.environ.get("JOB_ID")
num_images = os.environ.get("NUM_IMAGES")
credentials = os.environ.get("CREDENTIALS")
bucket_name = os.environ.get("BUCKET_NAME")

bucket = BucketAdapter(bucket_name, credentials)

for i in range(1, num_images + 1):
    bucket.download_file(f"{job_id}/inputs/{i}.jpg", f"images/zwx/zwx_{i}.jpg")