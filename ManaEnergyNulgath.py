import time
import random
import pyautogui
import pytesseract
import mss
import mss.tools
from PIL import Image
import io
from constants import *
from threading import Event
from shared_resources import typing_active, running, typing_lock
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as necessary

def open_inventory():
    x1, y1 = random.randint(INVENTORY_POS[0],INVENTORY_POS[1]), random.randint(INVENTORY_POS[2],INVENTORY_POS[3])
    pyautogui.click(x1,y1)
    time.sleep(random.uniform(2, 2.5))
    
def open_quest():
    x1, y1 = random.randint(QUEST_POS[0],QUEST_POS[1]), random.randint(QUEST_POS[2],QUEST_POS[3])
    pyautogui.click(x1,y1)
    time.sleep(random.uniform(1, 1.5))
    x2, y2 = random.randint(QUEST_POS_2[0],QUEST_POS_2[1]), random.randint(QUEST_POS_2[2],QUEST_POS_2[3])
    pyautogui.click(x2,y2)
    time.sleep(random.uniform(1, 1.5))
    
def search_for_item(item_name):
    with typing_lock:  # Acquire lock to ensure exclusive access to shared resources
        time.sleep(random.uniform(2, 2.5))
        # time.sleep(random.uniform(2, 2.5))
        typing_active.set()  # Pause other interfering activities
        try:
            x1, y1 = random.randint(SEARCH_BAR_POS[0], SEARCH_BAR_POS[1]), random.randint(SEARCH_BAR_POS[2], SEARCH_BAR_POS[3])
            pyautogui.click(x1, y1)
            pyautogui.typewrite(item_name)
            pyautogui.press('enter')
            time.sleep(random.uniform(2, 2.5))
        finally:
            typing_active.clear()  # Resume other activities, ensure the lock is released

def get_item_count():
    with mss.mss() as sct:
        # The screen part to capture
        # region = {'top': 224, 'left': 1740, 'width': 500, 'height': 500}
        region = INV_REGION
        img = sct.grab(region)

        # Save to file for inspection
        output_filename = 'screenshot.png'
        mss.tools.to_png(img.rgb, img.size, output=output_filename)
        print(f"Screenshot saved as {output_filename}")

        # Load the image from bytes for pytesseract
        img_rgb = mss.tools.to_png(img.rgb, img.size)
        text = pytesseract.image_to_string(Image.open(io.BytesIO(img_rgb)))

        # Process the OCR text to extract numbers
        count_text = ''.join(filter(str.isdigit, text))
        print(count_text)
        return int(count_text) if count_text.isdigit() else 0

def rand_path_calculator(path):
    pos_1 = random.randint(path[0][0],path[0][1]), random.randint(path[0][2],path[0][3])
    pos_2 = random.randint(path[1][0],path[1][1]), random.randint(path[1][2],path[1][3])
    pos_3 = random.randint(path[2][0],path[2][1]), random.randint(path[2][2],path[2][3])
    
    path = (pos_1, pos_2, pos_3)
    return path
    
def move_character(path):
    with typing_lock:
        time.sleep(random.uniform(2, 2.5))
        typing_active.set()
        print("Moving character, other actions paused.")
    try:
        path = rand_path_calculator(path)
        for coords in path:
            if not running.is_set():
                break
            pyautogui.click(coords)
            time.sleep(random.uniform(2.5, 3))
    finally:
        with typing_lock:
            typing_active.clear()
            print("Character move completed, actions resumed.")

def turn_in(minutes1, minutes2):
    open_quest()
    # Check if the quest is completed
    if check_for_completion():
        # Open quest
        time.sleep(random.uniform(2.5, 3))
        x1, y1 = random.randint(FIRST_QUEST_POS[0],FIRST_QUEST_POS[1]), random.randint(FIRST_QUEST_POS[2],FIRST_QUEST_POS[3])
        pyautogui.click(x1, y1)
        # Turn in quest
        time.sleep(random.uniform(2.5, 3))
        x2, y2 = random.randint(TURN_IN_POS[0],TURN_IN_POS[1]), random.randint(TURN_IN_POS[2],TURN_IN_POS[3])
        pyautogui.click(x2, y2)
    # Close quest
    time.sleep(random.uniform(2.5, 3))
    open_quest()
    time.sleep(random.uniform(minutes1, minutes2))

def check_for_completion():
    time.sleep(2)  # Ensure the screen has updated to reflect any changes
    with mss.mss() as sct:
        # region = {'top': 350, 'left': 175, 'width': 700, 'height': 700}
        region = QUEST_REGION
        img = sct.grab(region)
        output_filename = 'check_completion.png'
        mss.tools.to_png(img.rgb, img.size, output=output_filename)
        print(f"Screenshot for completion check saved as {output_filename}")

        try:
            # Load the image from saved file
            loaded_img = Image.open(output_filename)
            text = pytesseract.image_to_string(loaded_img)  # Using a specific psm might help
            print(f"Detected text: {text}")

            if "COMPLETE" in text.upper():
                print("Quest is completed.")
            else:
                print("Quest is NOT completed.")
            return "COMPLETE" in text.upper()

        except IOError as e:
            print(f"Error opening or reading image file: {e}")
            return False
    
def handle_quests(item_count):
    # pyautogui.press('l')  # Open quests
    # time.sleep(2)
    if(item_count > 1):
        for _ in range(item_count-1):
            turn_in(35,40)
            
def manage_mana_energy_quest():
    while running.is_set():
        time.sleep(random.uniform(60, 65))
        if not running.is_set(): break  # Check before continuing

        open_inventory()  # Open inventory
        search_for_item("Mana Energy for Nulgath")
        if not running.is_set(): break  # Check before continuing

        item_count = get_item_count()
        open_inventory()  # Close inventory
        if not running.is_set() or item_count <= 1: break  # Check before continuing

        move_character(ELEMENTAL_PATH_OUT)
        time.sleep(random.uniform(35, 40))
        if not running.is_set(): break  # Check before continuing

        handle_quests(item_count)
        move_character(ELEMENTAL_PATH_IN)  # Ensure you define this in constants.py
        if not running.is_set(): break  # Check before continuing

        time.sleep(random.uniform(60, 70))  # Wait before repeating or exiting
