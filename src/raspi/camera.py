#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timezone, timedelta
import os
import tweepy
from time import time, sleep
try:
    import picamera
except Exception:
    print('no raspi.');
from raspi import gesture
from raspi.led import LED

class Camera(object):
    def __init__(self):
        # 各種キーをセット
        self.CONSUMER_KEY = 'iTZxpCDtC37pIyRvxmHyUzAxY'
        self.CONSUMER_SECRET = 'WiEFajr56u0qwSJwbizhjzUyHVYPubsXUAugl5sQxTC5JJmeZW'
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)

        self.ACCESS_TOKEN = '827693598988603392-g4IJNK2MkEB8zABIygIJkRI3Cm7o6bs'
        self.ACCESS_SECRET = '7kX3LtDRVS480bvTWzdDmoVJjMnXdymzFWwEytVLEVVON'
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)

        # APIインスタンスを作成
        self.api = tweepy.API(self.auth)

        self.dst_filename = ""
        # これだけで、Twitter APIをPythonから操作するための準備は完了。
        print('Auth Done!')

        self.led = LED()

    def action(self):
        print('Camera action')
        
        # 3秒数える
        for i in range(60):
            if i in [0, 20, 40, 60]:
                self.led.blue_led_on()
            elif i in [10, 30, 50]:
                self.led.blue_led_off()

            # ジェスチャー取得
            class_name = gesture.judge()
            # カメラのジェスチャーでなくなったらLED消灯して終了
            if class_name != 'Camera':
                # 青LED消灯
                self.led.blue_led_off()
                self.led.cleanup()
                return

            sleep(0.05)
        
        # 青LEDを消灯、赤LED点灯
        self.led.blue_led_off()
        self.led.red_led_on()
        
        print('capture')

        # 現在時刻取得（画像ファイル名に利用）
        date = datetime.fromtimestamp(time(), timezone(timedelta(hours=+9), 'JST')).strftime('%Y%m%d-%H%M%S')
        
        # カメラ撮影
        try:
            camera = picamera.PiCamera()
            self.dst_filename = os.path.abspath(os.path.dirname(__file__)) + '/../../resource/camera/' + date + '.jpg'
            camera.capture(self.dst_filename)
            camera.close()
        except Exception as e:
            print(e, 'error occurred')
        
        # 赤消灯、青点灯
        self.led.red_led_off()
        self.led.blue_led_on()
        
        print('captured')

        # ツイート
        self.tweet()

        # 青消灯
        self.led.blue_led_off()
        self.led.cleanup()

    def tweet(self):
        # 内容の決定
        img_filename = self.dst_filename
        message = "HACK TIME!!\n" + datetime.fromtimestamp(time(), timezone(timedelta(hours=+9), 'JST')).strftime('%Y/%m/%d %p%I:%M')

        # 投稿
        self.api.update_with_media(
            filename = img_filename,
            status = message)

        os.remove(self.dst_filename)
        print("Tweeted")

def main():
    camera = Camera()
    camera.action()

if __name__ == '__main__':
    main()
