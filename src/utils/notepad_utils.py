import pyautogui
import time
from config import Config

def launch_notepad():
    try:
        pyautogui.press('winleft')
        time.sleep(1)
        pyautogui.write('notepad')
        pyautogui.press('enter')
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error launching Notepad: {e}")
        return False

def clear_notepad():
    try:
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.press('del')
        time.sleep(0.5)
        return True
    except Exception as e:
        print(f"Error clearing Notepad: {e}")
        return False

def type_post_content(post):
    try:
        clear_notepad()
        pyautogui.write(f"Title: {post['title']}\n\n", interval=Config.TYPE_INTERVAL)
        time.sleep(0.5)  # Delay after writing title
        pyautogui.write(f"post:\n{post['body']}\n", interval=Config.TYPE_INTERVAL)
        time.sleep(1)  # Delay after writing and before saving
        return True
    except Exception as e:
        print(f"Error typing content: {e}")
        return False

def save_document(file_path):
    try:
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('del')
        pyautogui.write(str(file_path.resolve()), interval=0.03)
        pyautogui.press('enter')
        time.sleep(1)
        return True
    except Exception as e:
        print(f"Error saving document: {e}")
        return False


def close_notepad():
    """Close only Notepad window"""
    try:
        for window in pyautogui.getAllWindows():
            if "Notepad" in window.title:
                window.activate()
                time.sleep(0.5)
                window.close()
                time.sleep(1)
                break  
        return True
    except Exception as e:
        print(f"Error closing Notepad: {e}")
        return False

def clear_project_directory():
    """
    Deletes all files in the tjm-project directory if it exists.
    """
    try:
        base_dir = Config.BASE_DIR
        if base_dir.exists() and base_dir.is_dir():
            for file in base_dir.glob("*"):
                if file.is_file():
                    file.unlink()
        print(f"Cleared all files in: {base_dir}")
        return True
    except Exception as e:
        print(f"Error clearing project directory: {e}")
        return False
