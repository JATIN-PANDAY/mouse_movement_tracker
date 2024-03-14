import pyautogui
import time

interval = 10

last_position = pyautogui.position()

last_move_time = time.time()

try:

    while True:
        current_position = pyautogui.position()

        if current_position != last_position:
            last_move_time = time.time()
            last_position = current_position
        else:
            if time.time() - last_move_time >= interval:
                print("Mouse pointer not moved")
                break
                last_move_time = time.time()
        time.sleep(1)        
        
except KeyboardInterrupt:
    print("Timer stopped manually")






