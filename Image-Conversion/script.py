#!/usr/bin/env python
import sys
from PIL import Image


def main():
    """Script to Convert JPEG to PNG"""
    source = sys.argv[1]
    destination = sys.argv[2]
    im1 = Image.open(source)
    im1.save(destination)
    return 0


if __name__ == "__main__":
    main()
