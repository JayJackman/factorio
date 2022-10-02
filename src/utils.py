"""
Filename: utils.py
Date Created: 6/4/2021
"""

from PIL import ImageTk, Image


def getIcon(filename):
    imageType = filename.split('/')[3]
    image = None
    if imageType == 'tiered':
        image = Image.open(filename).crop(box=(64, 0, 64 + 32, 32))
    elif imageType == 'single_64x64':
        image = Image.open(filename).resize((32, 32))

    return ImageTk.PhotoImage(image)


def emptyCallback(*args):
    pass
