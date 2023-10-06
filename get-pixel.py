from PIL import ImageGrab
import pyautogui

while True:
    mouse_pos = pyautogui.position()

    px = ImageGrab.grab().load()
    print("x: " + str(mouse_pos.x) + ", y: " + str(mouse_pos.y) + ", color: " + str(px[960, 540]))