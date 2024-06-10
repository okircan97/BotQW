# BotQW
A Python-based automation tool designed for interact with a game client, automating repetitive tasks.

# Objective: Developed a sophisticated automation tool in Python to interact with a game client, designed to automate repetitive tasks and manage game interactions dynamically.

# Core Technologies:
Python: Main programming language for scripting the automation logic.

pyautogui: Utilized for simulating mouse movements, clicks, and keyboard inputs to control the game GUI based on predefined logic.

tesseract-ocr: Integrated for optical character recognition (OCR) to read and interpret text directly from the game screen, allowing the tool to make decisions based on current game states and quests.

mss: Employed for fast and efficient screenshots, which are essential for the OCR operations and verifying the game state.

screeninfo: Used to fetch screen resolution dynamically, ensuring that the tool operates correctly on different monitors by adjusting coordinate calculations.

Multithreading: Applied Python's threading module to handle multiple operations simultaneously, such as monitoring game states, performing background tasks, and user interactions, without freezing the GUI.

Dynamic Coordinate Adjustment: Developed a function to scale mouse coordinates relative to the user's screen resolution, making the tool versatile across various display sizes.

Error Handling and Logs: Incorporated comprehensive error handling and logging mechanisms to trace steps and manage unexpected issues during runtime.

User Interface: Designed a simple yet functional graphical user interface (GUI) using tkinter, allowing users to interact with the tool, set parameters, and start/stop tasks.
