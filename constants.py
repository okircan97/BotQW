from screeninfo import get_monitors

# for monitor in get_monitors():
#     print(f"Width: {monitor.width}, Height: {monitor.height}")
    
monitor = get_monitors()[0]  # Assuming the first monitor is the target; adjust if necessary.
print(f"Primary Monitor - Width: {monitor.width}, Height: {monitor.height}")
    
# Scale the coordinates according to the monitor res.
def scale_res(x_start, x_end, y_start, y_end, width, height):
    return (int(x_start * width / 2560), int(x_end * width / 2560), int(y_start * height / 1440), int(y_end * height / 1440))
    
# Define class options
CLASSES = [
    "Basic Attack", "ArchPaladin", "Shaman",
    "Vampire Lord", "Void HighLord (Offensive)", "Void HighLord (Defensive)"
]

# Define quest options
QUESTS = ["None", "Seven Circles War", "Mana Energy for Nulgath", "Any Quest"]

# Monitor resolution
MONITOR_WIDTH = monitor.width
MONITOR_HEIGHT = monitor.height

# Regions
INV_REGION   = {'top': int(224*MONITOR_HEIGHT/1440), 'left': int(1740*MONITOR_WIDTH/2560), 'width': int(500*MONITOR_WIDTH/2560), 'height': int(500*MONITOR_HEIGHT/1440)} # Inventory region.
QUEST_REGION = {'top': int(350*MONITOR_HEIGHT/1440), 'left': int(175*MONITOR_WIDTH/2560),  'width': int(700*MONITOR_WIDTH/2560), 'height': int(700*MONITOR_HEIGHT/1440)}  # Quest bar region.
TEMP_REGION  = {'top': int(240*MONITOR_HEIGHT/1440), 'left': int(1660*MONITOR_WIDTH/2560), 'width': int(600*MONITOR_WIDTH/2560), 'height': int(600*MONITOR_HEIGHT/1440)} # Temp inventory region.

# Define coordinates for clicking actions if needed
MEGA_MEDAL_COORDINATES = scale_res(1500, 1550, 80, 120,MONITOR_WIDTH,MONITOR_HEIGHT)  # Example: (x_start, x_end, y_start, y_end)
WAR_MEDAL_COORDINATES  = scale_res(1600, 1650, 80, 120,MONITOR_WIDTH,MONITOR_HEIGHT)

# Quest related coordinates
FIRST_QUEST_POS  = scale_res(200, 500, 370, 390,MONITOR_WIDTH,MONITOR_HEIGHT)
QUEST_POS        = scale_res(1860, 1930, 1300, 1350,MONITOR_WIDTH,MONITOR_HEIGHT)
QUEST_POS_2      = scale_res(1800, 2000, 1145, 1170,MONITOR_WIDTH,MONITOR_HEIGHT)
TEMP_INVENTORY   = scale_res(1800, 2000, 1200, 1250,MONITOR_WIDTH,MONITOR_HEIGHT)
INVENTORY_POS    = scale_res(2400, 2460, 1300, 1350,MONITOR_WIDTH,MONITOR_HEIGHT)
SEARCH_BAR_POS   = scale_res(1850, 2300, 70, 120,MONITOR_WIDTH,MONITOR_HEIGHT)
TURN_IN_POS      = scale_res(420, 650 ,1096, 1140,MONITOR_WIDTH,MONITOR_HEIGHT)
TURN_IN_MULTIPLE = scale_res(1030, 1245, 825, 850,MONITOR_WIDTH,MONITOR_HEIGHT)
DRAG_POS_START   = (1200*MONITOR_WIDTH/2560,725*MONITOR_HEIGHT/1440)
DRAG_POS_END     = (1410*MONITOR_WIDTH/2560,725*MONITOR_HEIGHT/1440)

# Movement coordinates for elemental
ELEMENTAL_POS_1 = scale_res(1450, 1700, 1140, 1160,MONITOR_WIDTH,MONITOR_HEIGHT)
ELEMENTAL_POS_2 = scale_res(700, 900, 850, 900,MONITOR_WIDTH,MONITOR_HEIGHT)
ELEMENTAL_POS_3 = scale_res(1800, 2000, 1080, 1095,MONITOR_WIDTH,MONITOR_HEIGHT) # 3 mob room
ELEMENTAL_POS_4 = scale_res(1300, 1340, 150, 180,MONITOR_WIDTH,MONITOR_HEIGHT)
ELEMENTAL_POS_5 = scale_res(1200, 1300, 200, 300,MONITOR_WIDTH,MONITOR_HEIGHT)
ELEMENTAL_PATH_OUT  = (ELEMENTAL_POS_1, ELEMENTAL_POS_2, ELEMENTAL_POS_3)
ELEMENTAL_PATH_IN   = (ELEMENTAL_POS_4, ELEMENTAL_POS_2, ELEMENTAL_POS_5)





