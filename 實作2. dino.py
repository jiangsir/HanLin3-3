import pyautogui
import sys
import time

time.sleep(5)
x = 146 + 400
y = 980
pyautogui.moveTo(x, y, duration=0.1)
while True:
    # dot = pyautogui.pixel(230, 542)
    # dot == (255,255,255)
    dot2 = pyautogui.pixelMatchesColor(x, y, (255, 255, 255))
    dot1 = pyautogui.pixelMatchesColor(x+20, y+20, (255, 255, 255))
    # dot3 = pyautogui.pixelMatchesColor(210,511,(255,255,255))
    # if (not dot1 or not dot2 or not dot3):
    print('dot1', dot1, f'{x},{y}')
    print('dot2', dot2)
    # pyautogui.press('space')
    # pyautogui.moveTo(x,y,duration=0.1)
    # time.sleep(3)
    if (not dot1 or not dot2):                           
        pyautogui.press('space')
