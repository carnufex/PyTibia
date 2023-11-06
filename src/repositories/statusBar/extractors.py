from src.shared.typings import BBox, GrayImage
from .config import barSize, statusBarOffset


# TODO: add unit tests
# TODO: add perf
def getHpBar(screenshot: GrayImage, heartPos: BBox) -> GrayImage:
    y0 = heartPos[1] + 5
    y1 = y0 + 1
    x0 = heartPos[0] + 13
    x1 = x0 + barSize
    return screenshot[y0:y1, x0:x1][0]


# TODO: add unit tests
# TODO: add perf
def getManaBar(screenshot: GrayImage, heartPos: BBox) -> GrayImage:
    y0 = heartPos[1] + 5
    y1 = y0 + 1
    x0 = heartPos[0] + 14
    x1 = x0 + barSize
    return screenshot[y0:y1, x0:x1][0]

def getStatusBar(screenshot: GrayImage, stopButtonPos: BBox) -> GrayImage:
    y0 = stopButtonPos[1]
    y1 = y0 + stopButtonPos[3]
    x0 = stopButtonPos[0] - statusBarOffset
    x1 = stopButtonPos[0]
    return screenshot[y0:y1, x0:x1]