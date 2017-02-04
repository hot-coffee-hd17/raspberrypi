#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

def get_values():
    '''
    全てのセンサーから値を取得して返す
    人差し指・小指の順
    '''
    from random import random
    return [random(), random()]


def main():
    print(get_values())


if __name__ == '__main__':
    main()
