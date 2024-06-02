import pyautogui as pag
import cv2
import numpy as np


x , y = 68 , 147
w ,h = 1013 , 569

def find_color(target_color, region):
    screen = pag.screenshot(region=region)
    screen_np = np.array(screen)

    for y in range(screen_np.shape[0]):
        for x in range(screen_np.shape[1]):
            if all(screen_np[y, x][:3] == target_color):
                return x + region[0], y + region[1]
    return None

target_color = (255,119,99)
region = (x ,y , w ,h)

for i in range(500):
    position = find_color(target_color ,region)
    if position:
        print(f"Found color at position: {position}")
        pag.click(position)
    else:
        print("Color not found")

