import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

#hit(key) function is use to press any key in keyboard with automatic operate that key feature.
def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 350):
        for j in range(300, 400):
            if data[i, j] < 90:
                hit("down")
                return

    for i in range(300,350):
        for j in range(400,480):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
       

  

