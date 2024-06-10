import time
import random
import pyautogui
import pytesseract
import mss
import mss.tools
from PIL import Image
import io
from constants import *
from ManaEnergyNulgath import open_quest
from shared_resources import mouse_lock
from PIL import Image, ImageEnhance, ImageFilter
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as necessary

def open_temp_inventory():
    x1, y1 = random.randint(QUEST_POS[0],QUEST_POS[1]), random.randint(QUEST_POS[2],QUEST_POS[3])
    pyautogui.click(x1,y1)
    time.sleep(random.uniform(1, 1.5))
    x2, y2 = random.randint(TEMP_INVENTORY[0],TEMP_INVENTORY[1]), random.randint(TEMP_INVENTORY[2],TEMP_INVENTORY[3])
    pyautogui.click(x2,y2)
    time.sleep(random.uniform(1, 1.5))
    
def click_war_medal():
    with mouse_lock:
        # Example coordinates for button one
        x1, y1 = random.randint(WAR_MEDAL_COORDINATES[0],WAR_MEDAL_COORDINATES[1]), random.randint(WAR_MEDAL_COORDINATES[2],WAR_MEDAL_COORDINATES[3])
        pyautogui.click(x1, y1)
    time.sleep(random.uniform(10, 15))

def click_mega_medal():
    with mouse_lock:
        # Example coordinates for button two
        x2, y2 = random.randint(MEGA_MEDAL_COORDINATES[0],MEGA_MEDAL_COORDINATES[1]), random.randint(MEGA_MEDAL_COORDINATES[2],MEGA_MEDAL_COORDINATES[3])
        pyautogui.click(x2, y2)
    time.sleep(random.uniform(60, 65))
        
def wrath_guards():
    with mouse_lock:
        if(check_temp_inventory()):
            open_quest()
            # Open quest
            time.sleep(random.uniform(2.5, 3))
            x1, y1 = random.randint(FIRST_QUEST_POS[0],FIRST_QUEST_POS[1]), random.randint(FIRST_QUEST_POS[2],FIRST_QUEST_POS[3])
            pyautogui.click(x1, y1)
            # Click turn in
            time.sleep(random.uniform(2.5, 3))
            x2, y2 = random.randint(TURN_IN_POS[0],TURN_IN_POS[1]), random.randint(TURN_IN_POS[2],TURN_IN_POS[3])
            pyautogui.click(x2, y2)
            # Choose quantity
            drag_quest_quantity()
            # Click turn in multiple
            x1, y1 = random.randint(TURN_IN_MULTIPLE[0],TURN_IN_MULTIPLE[1]), random.randint(TURN_IN_MULTIPLE[2],TURN_IN_MULTIPLE[3])
            pyautogui.click(x1,y1)
            # Close quest
            time.sleep(random.uniform(2.5, 3))
            open_quest()
    # Wait
    time.sleep(random.uniform(57,59))
    
def drag_quest_quantity():
    # Move the mouse to the start position
    # pyautogui.moveTo(1200,725)
    pyautogui.moveTo(DRAG_POS_START)
    time.sleep(0.5)  # Pause for half a second for stability

    # Press the mouse down to start the drag
    pyautogui.mouseDown()

    # Move the mouse to the end position while holding the button
    pyautogui.moveTo(DRAG_POS_END)
    time.sleep(0.5)  # Pause for half a second to ensure the drag completes

    # Release the mouse button to end the drag
    pyautogui.mouseUp()

def check_temp_inventory():
    # Open temp inventory
    open_temp_inventory()
    with mss.mss() as sct:
        # region = {'top': 240, 'left': 1660, 'width': 600, 'height': 600}
        region = TEMP_REGION
        img = sct.grab(region)
        
        # Convert screenshot to PNG in bytes
        img_bytes = mss.tools.to_png(img.rgb, img.size)
        
        # Use pytesseract to detect text in the screenshot
        text = pytesseract.image_to_string(Image.open(io.BytesIO(img_bytes)))
        
        # Normalize and trim the text
        normalized_text = text.strip().upper()
        print("Detected text:", normalized_text)
        
        # Close temp inventory
        open_temp_inventory()
        
        # Check if "WRATH GUARDS DEFEATED X60" is in the detected text
        if "WRATH GUARDS DEFEATED X60" in normalized_text:
            print("Wrath guards completed.")
        else:
            print("Wrath guards NOT completed.")
        
        return "WRATH GUARDS DEFEATED X60" in normalized_text  # Return the check result
