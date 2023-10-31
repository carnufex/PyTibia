import time
import cv2
import dxcam
import numpy as np
from typing import Callable, Union
import xxhash
from src.shared.typings import BBox, GrayImage
import win32gui
import win32ui
from PIL import Image
from ctypes import windll


# camera = dxcam.create(output_color='BGRA', output_idx=2)
latestScreenshot = None


# TODO: add unit tests
def cacheObjectPosition(func: Callable) -> Callable:
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None

    def inner(screenshot):
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if lastX != None and lastY != None and lastW != None and lastH != None:
            if hashit(screenshot[lastY:lastY + lastH, lastX:lastX + lastW]) == lastImgHash:
                return (lastX, lastY, lastW, lastH)
        res = func(screenshot)
        if res is None:
            return None
        lastX = res[0]
        lastY = res[1]
        lastW = res[2]
        lastH = res[3]
        lastImgHash = hashit(
            screenshot[lastY:lastY + lastH, lastX:lastX + lastW])
        return res
    return inner


# TODO: add unit tests
def hashit(arr: np.ndarray) -> int:
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).intdigest()


# TODO: add unit tests
def hashitHex(arr: np.ndarray) -> str:
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).hexdigest()


# TODO: add unit tests
def locate(compareImage: GrayImage, img: GrayImage, confidence: float = 0.85) -> Union[BBox, None]:
    match = cv2.matchTemplate(compareImage, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    if res[1] <= confidence:
        return None
    return res[3][0], res[3][1], len(img[0]), len(img)


# TODO: add unit tests
def locateMultiple(compareImg: GrayImage, img: GrayImage, confidence: float = 0.85) -> Union[BBox, None]:
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= confidence)
    resultList = []
    for pt in zip(*loc[::-1]):
        resultList.append((pt[0], pt[1], len(compareImg[0]), len(compareImg)))
    return resultList

def region_grabber():
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

    # im = Image.frombuffer('RGB',
    #     (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    #     bmpstr, 'raw', 'BGRX', 0, 1)

    # Convert the PIL image to a NumPy array
    im = np.frombuffer(bmpstr, dtype='uint8')
    im = im.reshape((bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4))

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        #PrintWindow Succeeded
        # Save the image as a PNG file
        # im.save("test.png")
        #print("TIME: ", end - start)
        im = np.array(im)
        return im
    else:
        print("Something went shit in region_grabber()")


# TODO: add unit tests
def getScreenshot() -> GrayImage:
    global camera, latestScreenshot
    screenshot = region_grabber()
    if screenshot is None:
        return latestScreenshot
    latestScreenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2GRAY)
    return latestScreenshot
