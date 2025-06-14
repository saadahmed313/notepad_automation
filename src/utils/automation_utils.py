import time
import pyautogui
from botcity.core import DesktopBot
from src.config import SAVE_DIR

class NotepadBot(DesktopBot):
    def __init__(self):
        super().__init__()
        # Configure failsafe
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

    def open_notepad(self):
        """Open Notepad using BotCity's execute"""
        try:
            self.execute("notepad.exe")
            time.sleep(2)  # Using time.sleep for initial wait
            return True
        except Exception as e:
            print(f"[ERROR] Could not open Notepad: {e}")
            return False

    def type_blog_post(self, text):
        """Type text using PyAutoGUI for better typing control"""
        pyautogui.write(text, interval=0.05)

    def save_file(self, filename):
        """Save file using hybrid approach"""
        # Use BotCity for Ctrl+S
        self.control_s()
        time.sleep(1)
        
        # Use PyAutoGUI for typing path
        pyautogui.write(str(SAVE_DIR / filename))
        pyautogui.press('enter')
        time.sleep(1)

    def close_notepad(self):
        """Close Notepad using BotCity's alt_f4"""
        self.alt_f4()
        time.sleep(1)
