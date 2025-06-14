import time
from pathlib import Path
from src.config import SAVE_DIR, NUM_POSTS
from src.utils.api_utils import fetch_post
from src.utils.automation_utils import NotepadBot

def prepare_workspace():
    """
    Cleans the workspace by:
    1. Deleting all files in SAVE_DIR if it exists
    2. Creating the directory if it doesn't exist
    """
    try:
        if SAVE_DIR.exists():
            for file in SAVE_DIR.glob('*'):
                if file.is_file():
                    file.unlink()
                    print(f"[INFO] Deleted: {file.name}")
            print(f"[INFO] Cleared existing directory: {SAVE_DIR}")
        else:
            SAVE_DIR.mkdir(parents=True)
            print(f"[INFO] Created directory: {SAVE_DIR}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to prepare workspace: {e}")
        return False

def main():
    # Prepare the workspace before starting
    if not prepare_workspace():
        print("[ERROR] Could not initialize workspace. Exiting.")
        return

    bot = NotepadBot()

    for post_id in range(1, NUM_POSTS + 1):
        post = fetch_post(post_id)
        if not post:
            print(f"[ERROR] Skipping Post {post_id} due to fetch failure.")
            continue

        print(f"[INFO] Processing Post {post_id}")

        # Attempt to open Notepad with retries
        max_retries = 3
        for attempt in range(max_retries):
            if bot.open_notepad():
                break
            print(f"[ERROR] Failed to open Notepad for Post {post_id}, attempt {attempt + 1}/{max_retries}")
            time.sleep(2)
        else:
            print(f"[ERROR] Could not open Notepad for Post {post_id}. Skipping.")
            continue

        time.sleep(1)  # Ensure Notepad is focused

        # Type the content in the specified format
        try:
            bot.type_blog_post("-" * 90 + "\n")
            bot.type_blog_post(f"Title: {post['title']}\n")
            bot.type_blog_post("-" * 90 + "\n")
            bot.type_blog_post(f"Post:\n{post['body']}\n")
            bot.type_blog_post("-" * 90)
        except Exception as e:
            print(f"[ERROR] Failed to type content for Post {post_id}: {e}")
            bot.close_notepad()
            continue

        # Save the file
        filename = f"post_{post_id}.txt"
        for attempt in range(max_retries):
            try:
                bot.save_file(filename)
                break
            except Exception as e:
                print(f"[ERROR] Failed to save Post {post_id}, attempt {attempt + 1}/{max_retries}: {e}")
                time.sleep(2)
        else:
            print(f"[ERROR] Could not save Post {post_id}. Skipping.")
            bot.close_notepad()
            continue

        # Close Notepad
        try:
            bot.close_notepad()
        except Exception as e:
            print(f"[ERROR] Failed to close Notepad for Post {post_id}: {e}")
        time.sleep(1)

    print("[SUCCESS] Automation completed successfully.")

if __name__ == "__main__":
    main()
