# Notepad Automation Script

This Python script automates fetching blog posts from the JSONPlaceholder API, typing them into Notepad, and saving them as text files in a `tjm-project` directory on the Desktop. It uses a hybrid approach with `BotCity` for opening, saving, and closing Notepad, `PyAutoGUI` for typing text, and `pywin32` for window focus management. The script includes robust error handling and produces files in a specific format with dash separators.

## Repository Structure
```
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
│       ├── automation_utils.py
```

## 🚀 Features
- Fetches the first 10 posts from the JSONPlaceholder API.
- Opens Notepad, types each post’s title and body in a formatted layout, and saves as `post_{id}.txt` in `tjm-project`.
- Clears and recreates the `tjm-project` directory before processing.
- Implements error handling with retries for Notepad launch, typing, saving, and API/file operations.
- Ensures reliable automation with `pywin32` for Notepad window focus management.
- Outputs files in the format:
  ```
  ------------------------------------------------------------------------------------------
  Title: <post title>
  ------------------------------------------------------------------------------------------
  Post:
  <post body>
  ------------------------------------------------------------------------------------------
  ```


## ✅ Prerequisites

- Python 3.8 or higher
- Windows operating system
- All required libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/notepad-automation.git
   cd notepad-automation
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python src/main.py
```

The script will:
- Clear and create the `tjm-project` directory on the Desktop.
- Fetch posts 1 to 10 from the JSONPlaceholder API.
- For each post:
  - Open Notepad.
  - Type the post’s title and body with dash separators.
  - Save as `post_{id}.txt`.
  - Close Notepad.
- Log progress and errors to the console.

## Configuration
Settings in `src/config.py`:
- `SAVE_DIR`: Output directory (`~/Desktop/tjm-project`).
- `API_URL`: JSONPlaceholder API endpoint (`https://jsonplaceholder.typicode.com/posts`).
- `NUM_POSTS`: Number of posts (default: 10).

Adjust these for different output locations or post counts. Typing speed and pauses are configured in `src/utils/automation_utils.py`:
- `pyautogui.PAUSE`: Pause between actions (default: 0.5 seconds).
- `interval` in `type_blog_post`: Delay between keypresses (default: 0.05 seconds).

Increase pauses for slower systems.

## Error Handling
The script implements robust error handling for:
- **Application Not Launching**:
  - `open_notepad()` catches exceptions during Notepad launch and retries up to 3 times, logging errors and skipping posts if unsuccessful.
- **UI Elements Not Found**:
  - `type_blog_post`, `save_file`, and `close_notepad` use `pywin32` to verify Notepad focus, raising exceptions if focus is lost.
  - `save_file` checks for the "Save As" dialog to ensure it closes.
  - Skips posts and closes Notepad on UI errors to prevent orphaned instances.
- **API and File Operations**:
  - `fetch_post()` catches `requests.RequestException` for API failures, returning `None` to skip posts.
  - `prepare_workspace()` handles file system errors, preventing crashes if the directory is inaccessible.
- **General Recovery**:
  - `main()` skips failed posts and ensures Notepad is closed on errors.
  - `pyautogui.FAILSAFE` is enabled to abort automation by moving the mouse to a screen corner.

## Notes
- **Screen Activity**: `PyAutoGUI` and `BotCity` require the screen to be active and not locked/minimized.
- **Notepad Dependency**: Assumes Notepad is accessible via `notepad.exe`.
- **Error Logging**: Errors are logged to the console; consider adding file-based logging for persistent debugging.
- **Sequential Processing**: Processes posts one at a time to avoid focus issues with multiple Notepad instances.

## ⚠️ Limitations of the Automation Script

1. **🪟 Windows-Only**  
   - The script relies on `notepad.exe` and Windows-specific keyboard shortcuts.  
   - It won't work on macOS or Linux without significant modifications.

2. **🖱️ PyAutoGUI Sensitivity**  
   The script's reliability depends heavily on the desktop environment. It may fail if:
   - Screen resolution or UI scaling settings change.
   - Another application steals focus during automation.
   - System lag causes delays to be inaccurate or missed.

3. **🧾 Dialog Handling Issues**  
   - There is no logic to handle Notepad dialogs like:
     - "Do you want to save changes?"
     - "File already exists. Overwrite?"
   - These dialogs may interrupt automation and lead to failed saves or unsaved files.

4. **🌐 Network Dependency**  
   - API requests depend on an active internet connection.
   - Any connectivity issue will result in failed fetches and skipped posts.

5. **⏱️ Sequential Processing**  
   - Each post is handled one-by-one.
   - Due to Notepad’s single-instance behavior, the process is slow and does not use concurrency.

6. **⚙️ Hardcoded Configuration**  
   Key parameters are fixed inside the script:
   - `SAVE_DIR`
   - `NUM_POSTS`
   - `API_URL`  
   
   🔧 **Better alternatives**:
   - Use **command-line arguments** with `argparse`.
   - Or read from **environment variables** using `os.environ`.



## Development
To contribute:
1. Fork the repository.
2. Create a branch: `git checkout -b feature-name`.
3. Make changes and test.
4. Commit: `git commit -m "Describe changes"`.
5. Push: `git push origin feature-name`.
6. Open a pull request.

## Dependencies
See `requirements.txt`:
- `requests==2.31.0`
- `botcity-framework-core==1.0.1`
- `pyautogui==0.9.54`


## License
MIT License (add a `LICENSE` file if desired).
