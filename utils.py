from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from cerberus import Validator
import json

class BucketAdapter:

    bucket = None

    # Constructor
    def __init__(self, project_id: str, bucket_name: str, credentials: str):

        credentials = json.loads(credentials)

        schema = {
            'type': {'type': 'string', 'required': True},
            'project_id': {'type': 'string', 'required': True},
            'private_key_id': {'type': 'string', 'required': True},
            'private_key': {'type': 'string', 'required': True},
            'client_email': {'type': 'string', 'required': True},
            'client_id': {'type': 'string', 'required': True},
            'auth_uri': {'type': 'string', 'required': True},
            'token_uri': {'type': 'string', 'required': True},
            'auth_provider_x509_cert_url': {'type': 'string', 'required': True},
            'client_x509_cert_url': {'type': 'string', 'required': True},
            'universe_domain': {'type': 'string', 'required': True},
        }
        validator = Validator(schema)
        try:
            validator.validate(credentials)

            credentials = ServiceAccountCredentials.from_json_keyfile_dict(
                credentials
            )

            client = storage.Client(credentials=credentials, project=project_id)
            bucket = client.get_bucket(bucket_name)

            self.bucket = bucket
        except Exception as e:
            print(e)

    # Uploads a file to the bucket
    def upload_file(self, local_path, key):
        blob = self.bucket.blob(key)
        size = 1 * 1024 * 1024
        blob.upload_from_filename(local_path)

    # Downloads a file from the bucket
    def download_file(self, key, save_path):
        blob = self.bucket.blob(key)
        blob.download_to_filename(save_path)