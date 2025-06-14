# Notepad Automation Script

This Python script automates fetching blog posts from the JSONPlaceholder API, typing them into Notepad, and saving them as text files in a `tjm-project` directory on the Desktop. It uses PyAutoGUI for GUI automation and includes error handling for robust operation on Windows systems.

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
│       ├── file_utils.py
│       └── notepad_utils.py
```

## Features

- Fetches the first 10 posts from the JSONPlaceholder API.
- Opens Notepad, types each post’s title and body, and saves as `post <id>.txt` in `tjm-project`.
- Clears and recreates the `tjm-project` directory before processing.
- Includes error handling for application launch failures, UI element issues, API calls, and file operations.

## Prerequisites

- Python 3.8 or higher
- Windows operating system (required for Notepad)
- Dependencies listed in `requirements.txt`

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
1. Clear and create the `tjm-project` directory on the Desktop.
2. Fetch posts 1 to 10 from the JSONPlaceholder API.
3. For each post:
   - Open Notepad.
   - Type the post’s title and body.
   - Save as `post <id>.txt`.
   - Close Notepad.
4. Log progress and errors to the console.

## Configuration

Settings in `src/config.py`:
- `BASE_DIR`: Output directory (`~/Desktop/tjm-project`).
- `API_URL`: JSONPlaceholder API endpoint.
- `NUM_POSTS`: Number of posts (default: 10).
- `TYPE_INTERVAL`: Delay between keypresses (default: 0.05 seconds).
- `PAUSE_BETWEEN_ACTIONS`: Pause between PyAutoGUI actions (default: 0.5 seconds).

Adjust these for slower systems or different output locations.

## Error Handling

The script implements error handling for key failure scenarios:
- **Application Not Launching**:
  - `launch_notepad()` catches exceptions during Notepad launch (e.g., `Win + R`, typing `notepad`, or Enter key failures) and returns `False`, allowing the script to skip the post and continue.
  - Logs errors to the console (e.g., “Error launching Notepad: {e}”) for debugging.
- **UI Elements Not Found**:
  - `close_notepad()` iterates through windows using `pyautogui.getAllWindows()` to find and close Notepad, returning `False` if no Notepad window is found.
  - `save_document()` and `type_post_content()` use try-except blocks to handle potential UI issues (e.g., focus loss or dialog failures), ensuring Notepad is closed on error.
- **API Failures**:
  - `fetch_post()` catches `requests.RequestException` for network or API errors, returning `None` to skip the post without crashing.
- **File Operations**:
  - `setup_project_directory()` and `clear_project_directory()` handle file system errors (e.g., permission issues or directory deletion failures), preventing crashes and logging errors.
- **General Recovery**:
  - `main()` skips failed posts and calls `close_notepad()` on errors to prevent orphaned Notepad instances.
  - `pyautogui.FAILSAFE` is enabled, allowing manual termination by moving the mouse to the top-left corner.

## Notes

- **Screen Activity**: PyAutoGUI requires the screen to be active and not locked/minimized during execution.
- **Notepad Dependency**: Assumes Notepad is accessible via the `notepad` command in Windows.
- **Error Logging**: Errors are logged to the console; file-based logging can be added for persistent debugging.
- **Dialog Handling**: Currently lacks explicit handling for overwrite or unsaved changes dialogs, which may require manual intervention.

## Limitations

- **Windows-Only**: Relies on Notepad and Windows-specific shortcuts (e.g., `Win + R`).
- **PyAutoGUI Sensitivity**: May fail if:
  - Screen resolution or UI scaling changes.
  - Other applications steal focus (e.g., popups).
  - System lag exceeds fixed delays.
- **Dialog Handling**: No handling for “Save As” overwrite or unsaved changes dialogs, which may cause save/close failures.
- **No Retry Logic**: Lacks retries for transient failures (e.g., slow Notepad launch).
- **Network Dependency**: Requires an active internet connection for API requests.
- **Sequential Processing**: Slow due to Notepad’s single-instance nature and fixed delays.

## Troubleshooting

- **Notepad Not Launching**:
  - Increase `time.sleep(2)` in `launch_notepad()` or `PAUSE_BETWEEN_ACTIONS` in `config.py` for slower systems.
  - Ensure no applications intercept `Win + R`.
  - Verify `notepad.exe` is in `C:\Windows`.
- **Text Not Typing**:
  - Increase `TYPE_INTERVAL` or `PAUSE_BETWEEN_ACTIONS` in `config.py` (e.g., to 0.1 or 1.0).
  - Close other applications to prevent focus loss.
- **Files Not Saving**:
  - Check if `tjm-project` directory is writable.
  - Add overwrite dialog handling in `save_document()` (e.g., detect “Confirm Save As” and press ‘y’).
  - Run as administrator if access denied.
- **Notepad Not Closing**:
  - Add unsaved changes dialog handling in `close_notepad()` (e.g., press ‘n’ if dialog appears).
  - Manually close Notepad instances before rerunning.
- **General Issues**:
  - Run in a clean environment (close other applications).
  - Print `pyautogui.getAllWindows()` to debug window detection.

## Development

To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Make changes and test locally.
4. Commit changes: `git commit -m "Describe changes"`.
5. Push to your fork: `git push origin feature-name`.
6. Open a pull request.

## Dependencies

Listed in `requirements.txt`:
- `pyautogui==0.9.54`
- `requests==2.31.0`

## License

This project is licensed under the MIT License. Add a `LICENSE` file if desired.
