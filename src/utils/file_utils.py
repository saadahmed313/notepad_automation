import shutil
from pathlib import Path
from config import Config

def setup_project_directory():
    try:
        if Config.BASE_DIR.exists():
            shutil.rmtree(Config.BASE_DIR)
        Config.BASE_DIR.mkdir(parents=True)
        return True
    except Exception as e:
        print(f"Error setting up directory: {e}")
        return False

def get_file_path(post_id):
    return Config.BASE_DIR / f"post {post_id}.txt"