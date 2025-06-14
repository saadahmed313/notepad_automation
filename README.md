Notepad Automation Script
This Python script automates the process of fetching blog posts from the JSONPlaceholder API, typing them into Notepad, and saving them as text files in a tjm-project directory on the Desktop. It uses PyAutoGUI for GUI automation and includes error handling for robust operation on Windows systems.
Repository Structure
notepad-automation/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       ├── api_utils.py
│       ├── file_utils.py
│       └── notepad_utils.py

Features

Fetches the first 10 posts from the JSONPlaceholder API.
Opens Notepad, types each post’s title and body, and saves as post <id>.txt in tjm-project.
Clears and recreates the tjm-project directory before processing.
Includes error handling for application launch failures, UI element issues, and API/file operations.

Prerequisites

Python 3.8 or higher
Windows operating system (required for Notepad)
Dependencies listed in requirements.txt

Installation

Clone the repository:git clone https://github.com/<your-username>/notepad-automation.git
cd notepad-automation


Create a virtual environment (recommended):python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt



Usage
Run the script:
python src/main.py

The script will:

Clear and create the tjm-project directory on the Desktop.
Fetch posts 1 to 10 from the JSONPlaceholder API.
For each post:
Open Notepad.
Type the post’s title and body.
Save as post <id>.txt.
Close Notepad.


Log progress and errors to the console.

Configuration
Settings in src/config.py:

BASE_DIR: Output directory (~/Desktop/tjm-project).
API_URL: JSONPlaceholder API endpoint.
NUM_POSTS: Number of posts (default: 10).
TYPE_INTERVAL: Delay between keypresses (default: 0.05 seconds).
PAUSE_BETWEEN_ACTIONS: Pause between PyAutoGUI actions (default: 0.5 seconds).

Adjust these for slower systems or different output locations.
Error Handling
The script implements robust error handling for:

Application Not Launching:
launch_notepad() catches exceptions during Notepad launch (e.g., Win + R or notepad command failures) and returns False, allowing the script to skip the post.
Logs errors to the console for debugging.


UI Elements Not Found:
close_notepad() checks for Notepad windows using pyautogui.getAllWindows(), skipping closure if no window is found.
save_document() and type_post_content() use try-except blocks to handle failures (e.g., dialog not appearing or focus issues), ensuring Notepad is closed on error.


API and File Operations:
fetch_post() catches requests.RequestException for API failures, returning None to skip posts.
setup_project_directory() and clear_project_directory() handle file system errors, preventing crashes if the directory is inaccessible.


General Recovery:
main() skips failed posts and ensures Notepad is closed via close_notepad() on errors, preventing orphaned instances.
pyautogui.FAILSAFE is enabled to abort on mouse movement to the top-left corner.



Notes

Screen Activity: PyAutoGUI requires the screen to be active and not locked/minimized.
Notepad Dependency: Assumes Notepad is accessible via the notepad command.
Error Logging: Errors are logged to the console; consider adding file-based logging for persistent debugging.

Limitations

Windows-Only: Relies on Notepad and Windows shortcuts.
PyAutoGUI Sensitivity: May fail if:
Screen resolution or UI scaling changes.
Other applications steal focus.
System lag disrupts fixed delays.


Dialog Handling: Lacks explicit handling for overwrite or unsaved changes dialogs, which may cause save/close failures.
Network Dependency: Requires internet for API requests.
Sequential Processing: Slow due to Notepad’s single-instance nature.


Development
To contribute:

Fork the repository.
Create a branch: git checkout -b feature-name.
Make changes and test.
Commit: git commit -m "Describe changes".
Push: git push origin feature-name.
Open a pull request.

Dependencies
See requirements.txt:

pyautogui==0.9.54
requests==2.31.0

License
MIT License (add a LICENSE file if desired).
