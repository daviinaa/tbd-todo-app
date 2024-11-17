import os

FEATURE_FLAGS = {
    "ENABLE_NEW_UI": os.getenv("ENABLE_NEW_UI", "false").lower() == "true"
}
