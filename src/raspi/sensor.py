#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
try:
    import spidev
except:
    pass

# 圧力センサーの最大値・最小値（正規化に利用）
PRESS_MAX = 1023
PRESS_MIN = 0

def rand_val():
    ''' テスト用 '''
    import random
    return np.array([random.randint(PRESS_MIN, PRESS_MAX), random.randint(PRESS_MIN, PRESS_MAX)])


def from_sensors():
    spi = spidev.SpiDev()
    spi.open(0, 0)

    # 人差し指
    res1 = spi.xfer2([0x68, 0x00])
    val1 = (res1[0] * 256 + res1[1]) & 0x3ff

    # 小指
    res2 = spi.xfer2([0x78, 0x00])
    val2 = (res2[0] * 256 + res2[1]) & 0x3ff
    
    spi.close()
    return np.array([val1, val2])


def get_values():
    '''
    全てのセンサーから値を取得して返す
    人差し指・小指の順
    '''
    try:
        pressure = from_sensors()
    except Exception:
        pressure = rand_val()
    
    # 正規化して返す
    return list((pressure - PRESS_MIN) / (PRESS_MAX - PRESS_MIN))


def main():
    print(get_values())


if __name__ == '__main__':
    main()
