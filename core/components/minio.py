import os
from datetime import timedelta
from typing import List, Tuple
from core.components.base import INSTALLED_APPS
from dotenv import load_dotenv

load_dotenv()
if os.environ.get("ENABLE_MINIO", "False").lower() == "true":
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_USE_HTTPS = False
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    MINIO_URL_EXPIRY_HOURS = timedelta(days=7)
    MINIO_CONSISTENCY_CHECK_ON_START = True

    MINIO_BUCKET_PREFIX = os.getenv("MINIO_BUCKET_PREFIX", "app")
    MINIO_PRIVATE_BUCKETS = [
        f"{MINIO_BUCKET_PREFIX}-private",
    ]
    MINIO_PUBLIC_BUCKETS = [
        f"{MINIO_BUCKET_PREFIX}-munchkin-public",
    ]
    MINIO_POLICY_HOOKS: List[Tuple[str, dict]] = []
    MINIO_BUCKET_CHECK_ON_SAVE = True

    INSTALLED_APPS += [
        "django_minio_backend",
    ]
