# Idle-check

Keeps your system unlocked by moving cursor for windows 10.
If the user does not do any activity by cursor, the cursor will be automatically moved.

OS: Windows 10/ Ubuntu 20

Requirements:
* Python3
* pyautogui module to automate changing the cursor position.
* tqdm module to enable progress bar.
* For Ubuntu: python3-tk python3-dev

Usage
1. Install Python3
2. [ONLY UBUNTU] Install python libraries: sudo apt install python3-tk python3-dev
3. Install requirements.

   a) pip install -r requirements.txt
4. Configure timeout in the script.

   a) For changing the total runtime of script. Set the value of 'TOTAL_TIME'. Default is set to 8 hours.

   b) For changing the interval of moving cursor. Set the value of 'TIMEOUT'. Default is set to 2 mins.
5. Run the script

   a) python idle_check.py
