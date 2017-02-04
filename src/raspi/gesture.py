#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspi import sensor

# この値以上なら握っているとみなす
THRES_KOYUBI = 0.5
THRES_HITOSASHI = 0.7

def judge():
    '''
    センサーの値からジェスチャーを判定
    判定されたジェスチャーのクラス名かNoneを返す
    '''
    # センサの値取得
    sensor_values = sensor.get_values()
    print(sensor_values)

    if sensor_values[0] == 1 or sensor_values[1] == 1:
        # 1は誤作動なので例外
        return None
    elif sensor_values[0] >= THRES_HITOSASHI and sensor_values[1] < THRES_KOYUBI:
        return 'BoneSound'
    elif sensor_values[0] < THRES_HITOSASHI and sensor_values[1] >= THRES_KOYUBI:
        return 'Camera'
    elif sensor_values[0] >= THRES_HITOSASHI and sensor_values[1] >= THRES_KOYUBI:
        return 'Recorder'
    else:
        return None
