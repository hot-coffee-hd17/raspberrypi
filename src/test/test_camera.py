#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from raspi import camera

def main():
    instance = camera.Camera()
    instance.action()

if __name__ == '__main__':
    main()
