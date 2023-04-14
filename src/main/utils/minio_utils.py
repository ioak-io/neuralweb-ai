import os
from minio import Minio
from minio.error import S3Error
import joblib

BUCKET_NAME = "neuralweb-ai"

# https://medium.com/@erkansirin/storing-and-retrieving-scikit-learn-model-to-from-s3-f808457bc624


def save(model, path):
    _save_to_minio(model, path)


def load(path):
    return _load_from_minio(path)


def _get_minio_client():
    client = Minio(
        "localhost:8085",
        access_key="systemadmin",
        secret_key="systemadmin",
        secure=False
    )

    found = client.bucket_exists(BUCKET_NAME)
    if not found:
        client.make_bucket(BUCKET_NAME)
    else:
        print("Bucket 'neuralweb-ai' already exists")
    return client


def _save_to_minio(model, key):
    joblib.dump(model, key)
    minio_client = _get_minio_client()

    with open(key, 'rb') as file_data:
        file_stat = os.stat(key)
        minio_client.put_object(BUCKET_NAME, key,
                                file_data, file_stat.st_size)


def _load_from_minio(key):
    minio_client = _get_minio_client()
    minio_client.fget_object(BUCKET_NAME, key, key)
    model = joblib.load(key)
    return model
