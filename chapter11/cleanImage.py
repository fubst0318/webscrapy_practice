#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from PIL import Image
import subprocess
path = 'E:\\2018 U Books\\Python 网络数据收集\\python-scraping-master\\files\\'


def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # 对图片进行阈值过滤，然后保存
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(
        ["tesseract", filePath, " result -l eng ", path + "output.txt"])

    # 打开文件读取结果
    outputFile = open(path + 'output.txt', 'r')
    print(outputFile.read())
    outputFile.close()


if __name__ == '__main__':
    cleanFile(path + 'textBad.png', path + 'textNew.png')
