# Idle-check

Keeps your system unlocked by moving cursor for windows 10.
If the user does not do any activity by cursor, the cursor will be automatically moved.

OS: Windows 10

Requirements:
* Python3
* pyautogui module to automate changing the cursor position.
* tqdm module to enable progress bar.

Usage
1. Install Python3
2. Install requirements.
   >>pip install -r requirements.txt
3. Configure timeout in the script.
   -> For changing the total runtime of script. Set the value of 'TOTAL_TIME'. Default is set to 8 hours.
   -> For changing the interval of moving cursor. Set the value of 'TIMEOUT'. Default is set to 2 mins.
3. Run the script
   >>python idle_check.py
