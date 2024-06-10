import tkinter as tk
from tkinter import ttk
from threading import Thread, Event
import pyautogui
import time
import random
from constants import CLASSES, QUESTS, MEGA_MEDAL_COORDINATES, WAR_MEDAL_COORDINATES
from ManaEnergyNulgath import manage_mana_energy_quest, turn_in
from SevenCirclesWar import click_war_medal, click_mega_medal, wrath_guards
from shared_resources import typing_active, running

# from ManaEnergyNulgath import manage_mana_energy_quest  # Import the function
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Thread-safe method to update the GUI
def thread_safe_print(msg):
    def callback():
        text.insert(tk.END, msg + "\n")
        text.see(tk.END)
    root.after(1, callback)

# # Flag to control the typing and other automated key presses
# typing_active = Event()

def perform_key_actions():
    if mode.get() == "Vampire Lord":
        actions = [('5', 1, 1.5), ('3', 1, 1.5), ('4', 1, 1.5), ('2', 1, 1.5), ('3', 2, 2.4), ('4', 1, 1.5)]
    elif mode.get() == "Shaman":
        actions = [('2', 3, 3.5), ('3', 1.5, 1.75)]
    elif mode.get() == "ArchPaladin":
        actions = [('2', 1, 1.2),('4', 1, 1.2), ('2', 1, 1.2), ('3', 3, 3.2), 
                ('5', 1, 1.2), ('2', 5, 5.2), ('2', 1.2, 1.4), 
                ('3', 4, 4.2), ('2', 6, 6.2), ('3', 0, 0.2)]
    elif mode.get() == "Void HighLord (Offensive)":
        actions = [('4', 1.2, 1.4), ('5', 1.2, 1.4), ('3', 4.2, 4.4), 
                ('3', 1.2, 1.4)]
    elif mode.get() == "Void HighLord (Defensive)":
        actions = [('2', 1.2, 1.4), ('5', 1.2, 1.4), ('3', 4.2, 4.4), 
                ('3', 1.2, 1.4)]
    elif mode.get() == "Basic Attack":
        actions = [('1', 2.6, 2.8)]

    # Execute actions
    for key, min_time, max_time in actions:
        if not running.is_set():
            break
        pyautogui.press(key)
        thread_safe_print(f"Pressed '{key}'")
        sleep_duration = random.uniform(min_time, max_time)
        time.sleep(sleep_duration)
        
def random_press_key():
    while running.is_set():
        if not typing_active.is_set():
            perform_key_actions()
        time.sleep(0.1)  # Short sleep to prevent high CPU usage when waiting

def click_war_medal_ssw():
    while running.is_set() and quest.get() == "Seven Circles War":
        click_war_medal()

def click_mega_medal_ssw():
    while running.is_set() and quest.get() == "Seven Circles War":
        click_mega_medal()
        
def complete_wrath_guards():
    while running.is_set() and quest.get() == "Seven Circles War":
        wrath_guards()
        
def complete_quest(minutes1, minutes2):
    while running.is_set() and quest.get() == "Any Quest":
        turn_in(minutes1, minutes2)

def farm_mana_golem():
    while running.is_set() and quest.get() == "Mana Energy for Nulgath":
        manage_mana_energy_quest()
        if not running.is_set():
            break

def start_pressing():
    global pressing_thread, click_war_thread, click_mega_thread, wrath_guards_thread, mana_nulgath_thread, any_quest_thread
    if not running.is_set():
        running.set()
        typing_active.clear()
        pressing_thread = Thread(target=random_press_key, daemon=True)
        pressing_thread.start()
        
        if quest.get() == "Seven Circles War":
            click_war_thread = Thread(target=click_war_medal_ssw, daemon=True)
            click_war_thread.start()
            click_mega_thread = Thread(target=click_mega_medal_ssw, daemon=True)
            click_mega_thread.start()
            wrath_guards_thread = Thread(target=complete_wrath_guards, daemon=True)
            wrath_guards_thread.start()
        else:
            click_war_thread = None
            click_mega_thread = None
            wrath_guards_thread = None

        if quest.get() == "Mana Energy for Nulgath":
            mana_nulgath_thread = Thread(target=farm_mana_golem, daemon=True)
            mana_nulgath_thread.start()
        else:
            mana_nulgath_thread = None
            
        if quest.get() == "Any Quest":
            any_quest_thread = Thread(target=complete_quest, args=(35, 40), daemon=True)
            any_quest_thread.start()
        else:
            any_quest_thread = None
            

        start_button['state'] = tk.DISABLED
        stop_button['state'] = tk.NORMAL

def stop_pressing():
    running.clear()
    typing_active.set()  # Stop further key presses
    check_threads()

def check_threads():
    # Create a list of threads
    threads = [pressing_thread, click_war_thread, click_mega_thread, wrath_guards_thread, mana_nulgath_thread]
    all_joined = True

    for thread in threads:
        if thread is not None and thread.is_alive():
            all_joined = False
            break

    if all_joined:
        # Enable the start button once all threads have finished
        start_button['state'] = tk.NORMAL
        stop_button['state'] = tk.DISABLED
    else:
        # Recheck after some time
        root.after(100, check_threads)  # Check every 100 ms
    
# Initialize the root window
root = tk.Tk()
root.title("AQ Bot")

# Create the text widget
text = tk.Text(root, height=10, width=50)
text.pack()

# Define global variables
pressing_thread = None
mode = tk.StringVar(value=CLASSES[0])
quest = tk.StringVar(value=QUESTS[0])

# Create frames for a structured layout
class_frame = tk.Frame(root)
class_frame.pack(pady=5)
quest_frame = tk.Frame(root)
quest_frame.pack(pady=5)

# Mode selection setup
tk.Label(class_frame, text="Classes").pack(side=tk.TOP, fill=tk.X)
mode_combobox = ttk.Combobox(class_frame, textvariable=mode, values=CLASSES, state="readonly")
mode_combobox.pack(side=tk.BOTTOM, fill=tk.X)
mode_combobox.set(CLASSES[0])  # Set default value

# Quest selection setup
tk.Label(quest_frame, text="Quest").pack(side=tk.TOP, fill=tk.X)
quest_combobox = ttk.Combobox(quest_frame, textvariable=quest, values=QUESTS, state="readonly")
quest_combobox.pack(side=tk.BOTTOM, fill=tk.X)
quest_combobox.set(QUESTS[0])

# Button setup
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
start_button = tk.Button(button_frame, text="Start", command=start_pressing)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(button_frame, text="Stop", command=stop_pressing)
stop_button.pack(side=tk.LEFT, padx=10)
stop_button['state'] = tk.DISABLED

# Start the Tkinter event loop
root.mainloop()
