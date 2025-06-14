# main.py
import time
import pyautogui
from config import Config
from utils.api_utils import fetch_post
from utils.file_utils import setup_project_directory, get_file_path
from utils.notepad_utils import (
    launch_notepad,
    type_post_content,
    save_document,
    close_notepad,
    clear_project_directory
)

def main():
    """Main function to process posts"""
    print("Starting Notepad automation...")

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = Config.PAUSE_BETWEEN_ACTIONS

    # Clear existing files in project directory
    clear_project_directory()

    # Setup clean project directory
    if not setup_project_directory():
        print("Failed to setup project directory. Exiting.")
        return

    for post_id in range(1, Config.NUM_POSTS + 1):
        print(f"Processing post {post_id}...")

        post = fetch_post(post_id)
        if not post:
            continue

        if not launch_notepad():
            continue

        time.sleep(1.5)  # Wait for Notepad window to be ready

        if not type_post_content(post):
            close_notepad()
            continue

        time.sleep(1)  # Delay after typing before saving

        file_path = get_file_path(post_id)
        if not save_document(file_path):
            close_notepad()
            continue

        close_notepad()  # Ensure the current Notepad is closed before opening the next

        print(f"Successfully created post {post_id}")
        time.sleep(1)

    print("Automation completed.")

if __name__ == "__main__":
    main()
