#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from PIL import Image, ImageFilter

if __name__ == '__main__':
    kitten = Image.open('kitten.jpg')
    blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
    blurryKitten.save('kitten_blurred.jpg')
    blurryKitten.show()
