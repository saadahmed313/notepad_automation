import os
from pathlib import Path

class Config:
    BASE_DIR = Path.home() / "Desktop" / "tjm-project"
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    NUM_POSTS = 10
    TYPE_INTERVAL = 0.05
    PAUSE_BETWEEN_ACTIONS = 0.5