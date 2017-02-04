#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# 圧力センサーの最大値・最小値（正規化に利用）
PRESS_MAX = 100
PRESS_MIN = 0

def rand_val():
    ''' テスト用 '''
    import random
    return np.array([random.randint(PRESS_MIN, PRESS_MAX), random.randint(PRESS_MIN, PRESS_MAX)])


def from_sensors():
    import spidev

    # 人差し指
    spi1 = spidev.SpiDev()
    spi1.open(0, 0)
    res1 = spi1.xfer2([0x68, 0x00])
    val1 = (res1[0] * 256 + res1[1]) & 0x3ff

    # # 小指
    # spi2 = spidev.SpiDev()
    # spi2.open(0, 0)
    # res2 = spi2.xfer2([0x68, 0x00])
    # val2 = (res1[0] * 256 + res2[1]) & 0x3ff
    from random import randint
    val2 = randint(PRESS_MIN, PRESS_MAX)
    
    return np.array([val1, val2])


def get_values():
    '''
    全てのセンサーから値を取得して返す
    人差し指・小指の順
    '''
    pressure = from_sensors()

    # 正規化して返す
    return list((pressure - PRESS_MIN) / (PRESS_MAX - PRESS_MIN))


def main():
    print(get_values())


if __name__ == '__main__':
    main()
