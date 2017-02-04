#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from raspi import led
import time

def main():
    instance = led.LED()
    instance.red_led_on()
    time.sleep(3)
    instance.red_led_off()
    time.sleep(3)
    instance.red_led_flash()
    time.sleep(3)
    instance.red_led_off()
    time.sleep(3)

if __name__ == '__main__':
    main()
