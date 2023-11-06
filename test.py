# import src.repositories.gameWindow.creatures as gameWindowCreatures
# import src.utils.core
# import src.repositories.battleList.core
# import src.repositories.battleList.extractors
# import src.repositories.gameWindow.config
# import src.repositories.gameWindow.core



# grayScreenshot = src.utils.core.getScreenshot()
# radarCoordinate = src.repositories.radar.core.getCoordinate(grayScreenshot)
# content = src.repositories.battleList.extractors.getContent(grayScreenshot)
# battleListCreatures = src.repositories.battleList.core.getCreatures(content)
# beingAttackedCreatureCategory = src.repositories.battleList.core.getBeingAttackedCreatureCategory(battleListCreatures)
# gameWindowSize = src.repositories.gameWindow.config.gameWindowSizes[1080]
# gameWindowCoordinate = src.repositories.gameWindow.core.getCoordinate(grayScreenshot, gameWindowSize)
# gameWindowImg = src.repositories.gameWindow.core.getImageByCoordinate(grayScreenshot, gameWindowCoordinate, gameWindowSize)
# gameWindowCreaturess = src.repositories.gameWindow.creatures.getCreatures(battleListCreatures, 'left', gameWindowCoordinate, gameWindowImg, radarCoordinate,beingAttackedCreatureCategory=beingAttackedCreatureCategory)
# isTrapped = gameWindowCreatures.isTrappedByCreatures(gameWindowCreaturess, radarCoordinate)

# print('isTrapped', isTrapped)


import time
import cv2
import dxcam
import numpy as np
from typing import Callable, Union
import xxhash
# from src.shared.typings import BBox, GrayImage
import win32gui
import win32ui
from PIL import Image
from ctypes import windll
import pathlib
from src.repositories.chat.core import getTabs, hasNewLoot, getLootLines
from src.utils.image import loadFromRGBToGray

from PIL import Image


camera = dxcam.create(output_color='BGRA', output_idx=2)
latestScreenshot = None



def region_grabber():
    start = time.time()
    hwnd = win32gui.FindWindow(None, 'Fullscreen Projector (Scene) - Scene')


    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = int(right - left)
    h = int(bot - top)

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area.
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    # print(result)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer('RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    # Convert the PIL image to a NumPy array
    # im = np.frombuffer(bmpstr, dtype='uint8')
    # im = im.reshape((bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4))

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        #PrintWindow Succeeded
        # Save the image as a PNG file
        # im.save("test.png")
        end = time.time()
        #print("TIME: ", end - start)
        im = np.array(im)
        return im
    else:
        print("Something went shit in region_grabber()")


# TODO: add unit tests
def getScreenshot():
    global camera, latestScreenshot
    # screenshot = region_grabber()
    screenshot = camera.grab()
    Image.fromarray(screenshot).show()
    if screenshot is None:
        return latestScreenshot
    latestScreenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2GRAY)
    return latestScreenshot






while True:
    try:
        fps = 1 / (time.time() - loop_time)
        print(f'FPS {fps}', flush=True)
    except:
        pass
    loop_time = time.time()
    x = getScreenshot()
    break
