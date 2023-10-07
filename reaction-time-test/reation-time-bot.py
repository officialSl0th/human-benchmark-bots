import pyautogui
import webbrowser
from time import sleep

webbrowser.open("https://humanbenchmark.com/tests/reactiontime", 1)
sleep(5)

# Define the target color
target_color = (116, 215, 119)

# Locate the initial position
position = pyautogui.locateOnScreen(image="./images/lightning.png", grayscale=True, confidence=.5)

if position is None:
    print("Correct test not found")
else:
    x = position.left - position.width / 2
    y = position.top - position.height / 2

    # Click on the initial position
    pyautogui.click(x, y)

    # Perform the clicks
    count = 0
    while count < 5:
        # Check if the pixel color matches the target color
        if pyautogui.pixelMatchesColor(x, y, target_color, tolerance=10):
            pyautogui.click(x, y)
            count += 1
            sleep(0.5)
            pyautogui.click(x, y)

# Add some delay to let the browser close
sleep(2)
