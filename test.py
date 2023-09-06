# from utils import BucketAdapter
# import json
# import os

# keyfile = open("keyfile.json", "r").read()


# adapter = BucketAdapter(
#     project_id='lively-antonym-396009',
#     bucket_name='envision-jobs',
#     credentials=keyfile
# )

# base_dir = "C:/Users/a/Desktop/umrx"
# imgs = os.listdir(base_dir)

# for i, path in enumerate(imgs):
#     adapter.upload_file(os.path.join(base_dir, path), f"1234/inputs/{i+1}.jpg")
#     print(f"Uploaded {path} to bucket")