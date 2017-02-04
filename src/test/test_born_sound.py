#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from raspi import bone_sound

import time

def main():
    instance = bone_sound.BoneSound()
    instance.action()
    time.sleep(1)
    instance = bone_sound.BoneSound()
    instance.action()

if __name__ == '__main__':
    main()
