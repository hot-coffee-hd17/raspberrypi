#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as RED_LED_GPIO
import RPi.GPIO as BLUE_LED_GPIO

class LED:
    def __init__(self):
        self.RED_LED_GPIO_PIN = 10
        self.BLUE_LED_GPIO_PIN = 11

        RED_LED_GPIO.setmode(RED_LED_GPIO.BCM)
        BLUE_LED_GPIO.setmode(BLUE_LED_GPIO.BCM)
        RED_LED_GPIO.setup(self.RED_LED_GPIO_PIN, RED_LED_GPIO.OUT)
        BLUE_LED_GPIO.setup(self.BLUE_LED_GPIO_PIN, BLUE_LED_GPIO.OUT)

    def red_led_on(self):
        RED_LED_GPIO.output(self.RED_LED_GPIO_PIN, RED_LED_GPIO.HIGH)

    def red_led_off(self):
        RED_LED_GPIO.output(self.RED_LED_GPIO_PIN, RED_LED_GPIO.OUT)

    def red_led_flash(self):
        RED_LED_GPIO.output(self.RED_LED_GPIO_PIN, RED_LED_GPIO.LOW)

    def blue_led_on(self):
        BLUE_LED_GPIO.output(self.BLUE_LED_GPIO_PIN, BLUE_LED_GPIO.HIGH)

    def blue_led_off(self):
        BLUE_LED_GPIO.output(self.BLUE_LED_GPIO_PIN, BLUE_LED_GPIO.OUT)

    def blue_led_flash(self):
        BLUE_LED_GPIO.output(self.BLUE_LED_GPIO_PIN, BLUE_LED_GPIO.LOW)
