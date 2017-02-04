#!/usr/bin/env python
# -*- coding: utf-8 -*-

# この値以上なら握っているとみなす
THRESHOLD = 0.7

def judge(sensor_values):
    '''
    センサーの値からジェスチャーを判定
    判定されたジェスチャーのクラス名かNoneを返す
    '''
    if sensor_values[0] >= THRESHOLD and sensor_values[1] < THRESHOLD:
        return 'BoneSound'
    elif sensor_values[0] < THRESHOLD and sensor_values[1] >= THRESHOLD:
        return 'Camera'
    elif sensor_values[0] >= THRESHOLD and sensor_values[1] >= THRESHOLD:
        return 'Recorder'
    else:
        return None
