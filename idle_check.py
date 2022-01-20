import time
import random
import pyautogui
from datetime import datetime

# If cursor moves to (0,0), pyautogui module gives exception.
# So for fixing that, set FAILSAFE to False
pyautogui.FAILSAFE = False

# Total time in seconds to run this script for checking idle state. Default value: 8 hours.
TOTAL_TIME = 60*60*8
# Time Interval for idle state check.
TIMEOUT = 120

# Calculate the count required to check for idle state.
MAX_COUNT = int(TOTAL_TIME//TIMEOUT)

class Cursor():
    def __init__(self):
        pos = pyautogui.position()
        self.xposition = pos.x
        self.yposition = pos.y
        self.time = datetime.now()

def switch_window():
    """
    Switch window using alt + tab.
    """
    try:
        pyautogui.keyDown("altleft")
        pyautogui.keyDown("tab")
        time.sleep(1)
        pyautogui.keyUp("altleft")
        pyautogui.keyUp("tab")
    except Exception as ex:
        print(f"Failed to switch window. Error: {ex}")

def move_cursor():
    """
    Move cursor to a random position between 1-500px in x and y co-ordinates.
    """
    random_x = random.randint(1, 500)
    random_y = random.randint(1, 500)
    try:
        pyautogui.moveTo(random_x, random_y, duration=1)
    except Exception as ex:
        print(f"Failed to move cursor. Error: {ex}")
        # Try to switch window if cursor movement failed
        switch_window()

def check_idle_state():
    """
    Check for idle state by comparing the last cursor position and idle timeout.
    """
    new_cursor = Cursor()
    td = new_cursor.time - CURRENT_CURSOR.time
    if td.total_seconds() >= TIMEOUT:
        if (new_cursor.xposition == CURRENT_CURSOR.xposition and
            new_cursor.yposition == CURRENT_CURSOR.yposition):
            print("IDLE!!")
            move_cursor()
        else:
            print("Not IDLE!!")
        time.sleep(1)
        # Update the current cursor value.
        new_cursor = Cursor()
        CURRENT_CURSOR.xposition = new_cursor.xposition
        CURRENT_CURSOR.yposition = new_cursor.yposition
        CURRENT_CURSOR.time = new_cursor.time
    else:
        print("Less than idle timeout")

CURRENT_CURSOR = Cursor()
counter = 0

def progress_bar(duration):
    from tqdm import tqdm
    for i in tqdm(range(duration), ascii=True):
        time.sleep(1)

while(counter <= MAX_COUNT):
    try:
        progress_bar(TIMEOUT)
    except:
        time.sleep(TIMEOUT)
    check_idle_state()
    print(f"Count: {counter}/{MAX_COUNT}")
    print(f"{CURRENT_CURSOR.xposition} {CURRENT_CURSOR.yposition} {CURRENT_CURSOR.time}")
    counter = counter + 1
