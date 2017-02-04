#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import re
from raspi import sensor
from raspi import gesture

# 何秒毎にセンサーをチェックするか
FRAME_RATE = 1


def to_snakecase(str):
    ret = re.sub(r'([\s|A-Z])', "_\\1", str)
    ret = re.sub(r'([\s])', "",ret)
    ret = re.sub(r'^_', "",ret)
    return ret.lower()


def main():
    while True:
        # センサの値取得
        sensor_values = sensor.get_values()

        # ジェスチャー判定
        class_name = gesture.judge(sensor_values)
        print('** ' ,sensor_values, class_name)

        # ジェスチャーであると判定されたら対応するアクション実行
        if class_name is not None:
            mod = __import__('raspi.' + to_snakecase(class_name), fromlist=[class_name])
            instance = getattr(mod, class_name)()
            instance.action()

        time.sleep(FRAME_RATE)


if __name__ == '__main__':
    main()
