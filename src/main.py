#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from raspi import sensor
from raspi import gesture

# 何秒毎にセンサーをチェックするか
FRAME_RATE = 1


def main():
    while True:
        # センサの値取得
        sensor_values = sensor.get_values()

        # ジェスチャー判定
        class_name = gesture.judge(sensor_values)
        
        # ジェスチャーであると判定されたら対応するアクション実行
        if class_name is not None:
            mod = __import__('raspi.' + class_name.lower(), fromlist=[class_name])
            instance = getattr(mod, class_name)()
            instance.action()

        print('wait')
        time.sleep(FRAME_RATE)


if __name__ == '__main__':
    main()
