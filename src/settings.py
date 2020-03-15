import os
from dotenv import load_dotenv
load_dotenv()

LOGURU_RETENTION = os.getenv("LOGURU_RETENTION")
LOGURU_ROTATION = os.getenv("LOGURU_ROTATION")