import requests
from config import Config

def fetch_post(post_id):
    try:
        response = requests.get(f"{Config.API_URL}/{post_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching post {post_id}: {e}")
        return None
