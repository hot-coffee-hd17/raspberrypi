#!/usr/bin/env python
# -*- coding: utf-8 -*-
import picamera
from datetime import datetime
import os

class Camera(object):
    def __init__(self):
        pass

    def action(self):
        print('camera action')

        # 現在時刻取得（画像ファイル名に利用）
        date = datetime.now().strftime('%Y%m%d-%H%M%S')
        
        camera = picamera.PiCamera()
        camera.capture(os.path.abspath(os.path.dirname(__file__)) 
            + '/../resources/camera/'
            + date
            + '.jpg'
            )


def main():
    camera = Camera()
    camera.action()


if __name__ == '__main__':
    main()
