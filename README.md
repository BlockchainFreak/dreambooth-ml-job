# Python Training Application

## Cloud Infrastructure

We are using Google Vertex AI as our cloud infrastructure. A custom Image made from the Dockerfile is hosted on Google Container Registry. It fetches the current git Repo and runs the `start.sh` shell script.

## Read and write Cloud Storage files with Cloud Storage FUSE

In all custom training jobs, Vertex AI mounts Cloud Storage buckets that you have access to in the /gcs/ directory of each training node's file system. As a convenient alternative to using the Python Client for Cloud Storage or another library to access Cloud Storage, you can read and write directly to the local file system in order to read data from Cloud Storage or write data to Cloud Storage. For example, to load data from gs://BUCKET/data.csv, you can use the following Python code:

```python
file = open('/gcs/BUCKET/data.csv', 'r')
```

Vertex AI uses Cloud Storage FUSE to mount the storage buckets. Note that directories mounted by Cloud Storage FUSE are not POSIX compliant.

The credentials that you are using for custom training determine which buckets you can access in this way. The preceding section about which resources your code can access describes exactly which buckets you can access by default and how to customize this access.