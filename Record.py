from pynput.mouse import Listener as MouseListener, Controller as MouseController, Button
from pynput.keyboard import Listener as KeyboardListener, Controller as KeyboardController, Key
import time
import json
import os

recorded_actions = []
stop_recording = False

def on_move(x, y):
    global stop_recording
    recorded_actions.append(('move', (x, y), time.time()))
    print(f"Recorded move: {x}, {y}")
    if (x, y) == (0, 0):
        print("[*] Mouse moved to (0, 0), stopping recording.")
        stop_recording = True
        return False

def on_click(x, y, button, pressed):
    recorded_actions.append((
        'click',
        (x, y, button.name, 'press' if pressed else 'release'),
        time.time()
    ))
    print(f"Recorded click: {x}, {y}, {button.name}, {'press' if pressed else 'release'}")

def on_scroll(x, y, dx, dy):
    recorded_actions.append(('scroll', (x, y, dx, dy), time.time()))
    print(f"Recorded scroll: {x}, {y}, {dx}, {dy}")

def on_press(key):
    try:
        recorded_actions.append(('key_press', (key.char,), time.time()))
        print(f"Recorded key press: {key.char}")
    except AttributeError:
        recorded_actions.append(('key_press', (str(key),), time.time()))
        print(f"Recorded key press: {str(key)}")

def on_release(key):
    try:
        recorded_actions.append(('key_release', (key.char,), time.time()))
        print(f"Recorded key release: {key.char}")
    except AttributeError:
        recorded_actions.append(('key_release', (str(key),), time.time()))
        print(f"Recorded key release: {str(key)}")

def start_record():
    global stop_recording
    stop_recording = False
    print("[*] Recording started. Move/click/scroll/type. Move cursor to (0, 0) to stop.")

    start_time = time.time()

    mouse_listener = MouseListener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll
    )
    keyboard_listener = KeyboardListener(
        on_press=on_press,
        on_release=on_release
    )

    mouse_listener.start()
    keyboard_listener.start()

    try:
        while not stop_recording:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("[*] KeyboardInterrupt received, stopping early.")
        stop_recording = True

    mouse_listener.stop()
    keyboard_listener.stop()
    mouse_listener.join()
    keyboard_listener.join()
    print("[*] Recording stopped.")

    if recorded_actions:
        normalized = []
        for action_type, data, ts in recorded_actions:
            normalized.append((action_type, data, ts - start_time))

        out_path = 'mouse_keyboard_record.json'
        with open(out_path, 'w') as f:
            json.dump(normalized, f, indent=2)

        print(f"[*] Recorded {len(normalized)} actions.")
        print(f"[*] Saved to {os.path.abspath(out_path)}")
    else:
        print("[*] No actions were recorded.")

if __name__ == '__main__':
    start_record()
