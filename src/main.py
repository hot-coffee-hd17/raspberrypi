#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import re

from raspi import gesture

# 何秒毎にセンサーをチェックするか
FRAME_RATE = 0.05

def to_snakecase(str):
    ret = re.sub(r'([\s|A-Z])', "_\\1", str)
    ret = re.sub(r'([\s])', "",ret)
    ret = re.sub(r'^_', "",ret)
    return ret.lower()

def main():
    while True:
        # ジェスチャー判定
        class_name = gesture.judge()
        print('** ', class_name)

        # ジェスチャーであると判定されたら対応するアクション実行
        if class_name is not None:
            mod = __import__('raspi.' + to_snakecase(class_name), fromlist=[class_name])
            instance = getattr(mod, class_name)()
            instance.action()

        time.sleep(FRAME_RATE)


if __name__ == '__main__':
    main()
