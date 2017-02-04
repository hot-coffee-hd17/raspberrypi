#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class LED:
    def __init__(self):
        self.RED_LED_GPIO_PIN = 10
        self.BLUE_LED_GPIO_PIN = 18

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RED_LED_GPIO_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_LED_GPIO_PIN, GPIO.OUT)

    def red_led_on(self):
        GPIO.output(self.RED_LED_GPIO_PIN, GPIO.HIGH)

    def red_led_off(self):
        GPIO.output(self.RED_LED_GPIO_PIN, GPIO.OUT)

    def red_led_flash(self):
        GPIO.output(self.RED_LED_GPIO_PIN, GPIO.LOW)

    def blue_led_on(self):
        GPIO.output(self.BLUE_LED_GPIO_PIN, GPIO.HIGH)

    def blue_led_off(self):
        GPIO.output(self.BLUE_LED_GPIO_PIN, GPIO.OUT)

    def blue_led_flash(self):
        GPIO.output(self.BLUE_LED_GPIO_PIN, GPIO.LOW)
