#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspi import sensor

# この値以上なら握っているとみなす
THRESHOLD = 0.7

def judge():
    '''
    センサーの値からジェスチャーを判定
    判定されたジェスチャーのクラス名かNoneを返す
    '''
    # センサの値取得
    sensor_values = sensor.get_values()

    if sensor_values[0] == 1 or sensor_values[1] == 1:
        # 1は誤作動なので例外
        return None
    elif sensor_values[0] >= THRESHOLD and sensor_values[1] < THRESHOLD:
        return 'BoneSound'
    elif sensor_values[0] < THRESHOLD and sensor_values[1] >= THRESHOLD:
        return 'Camera'
    elif sensor_values[0] >= THRESHOLD and sensor_values[1] >= THRESHOLD:
        return 'Recorder'
    else:
        return None
