import pyautogui

def Funny_def():
    while True:
        pixels_OF_black= pyautogui.pixelMatchesColor(105,131,(32,33,36) , tolerance=8)
        Pixel_of_dark= pyautogui.pixelMatchesColor(210,410,(250,250,46) , tolerance=8)
        if ((Pixel_of_dark == False and pixels_OF_black == False)):
            pyautogui.press("space")
        elif ((Pixel_of_dark == True and pixels_OF_black == True)):
            pyautogui.press("space")
Funny_def()