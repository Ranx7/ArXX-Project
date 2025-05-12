from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time
import json
def start_play():

    mouse = MouseController()
    keyboard = KeyboardController()


    with open('mouse_keyboard_record.json', 'r') as f:
        recorded_actions = json.load(f)

    print("[*] Replaying", len(recorded_actions), "actions...")
    start_time = time.time()

    for action in recorded_actions:
        action_type, data, delay = action
        time_to_wait = max(0, delay - (time.time() - start_time))
        time.sleep(time_to_wait)

        if action_type == 'move':
            x, y = data
            mouse.position = (x, y)

        elif action_type == 'click':
            x, y, button, press_type = data
            mouse.position = (x, y)
            btn = getattr(Button, button.lower())
            if press_type == 'press':
                mouse.press(btn)
            else:
                mouse.release(btn)

        elif action_type == 'scroll':
            x, y, dx, dy = data
            mouse.position = (x, y)  
            mouse.scroll(dx, dy)

        elif action_type == 'key_press':
            key = data[0]
            if key.startswith('Key.'):
        
                special_key = getattr(Key, key.split('.')[-1])
                keyboard.press(special_key)
            else:
                keyboard.press(key)

        elif action_type == 'key_release':
            key = data[0]
            if key.startswith('Key.'):
            
                special_key = getattr(Key, key.split('.')[-1])
                keyboard.release(special_key)
            else:
                keyboard.release(key)

    print("[*] Playback finished.")
