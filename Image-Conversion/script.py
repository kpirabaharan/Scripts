#!/usr/bin/env python
"""Script to Convert JPEG to PNG"""
import sys
import os
from PIL import Image


def normal():
    count = len(sys.argv)
    source = sys.argv[1]
    if count < 3:
        destination = source.split(".")[0] + ".png"
    else:
        destination = sys.argv[2]
    im1 = Image.open(source)
    im1.save(destination)
    return 0


def recursive():
    source = (
        sys.argv[2] if "~" in sys.argv[2] else os.path.expanduser(sys.argv[2])
    )

    source = source if source[-1] == "/" else source + "/"

    if os.path.isdir(source):
        files = os.listdir(source)
        for file in files:
            try:
                im1 = Image.open(source + file)
                destination = file.split(".")[0] + ".png"
                print(destination)
                im1.save(source + destination)
            except:
                print("Not an image file")
                continue
    else:
        print("Not a directory")
        return 1

    return 0


if __name__ == "__main__":
    print(sys.argv)
    if sys.argv[1] == "recursive":
        recursive()
    else:
        normal()
