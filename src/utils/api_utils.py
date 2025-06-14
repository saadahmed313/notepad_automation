import requests
from src.config import API_URL

def fetch_post(post_id):
    try:
        response = requests.get(f"{API_URL}/{post_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR] Failed to fetch post {post_id}: {e}")
        return None
