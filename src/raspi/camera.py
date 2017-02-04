#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import os
import tweepy
try:
    import picamera
except Exception:
    print('no raspi.');

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

    def action(self):
        print('Camera Captured')

        # 現在時刻取得（画像ファイル名に利用）
        date = datetime.now().strftime('%Y%m%d-%H%M%S')
        
        try:
            camera = picamera.PiCamera()
            self.dst_filename = os.path.abspath(os.path.dirname(__file__)) + '/../../resource/camera/' + date + '.jpg'
            camera.capture(self.dst_filename)
            camera.close()
        except Exception as e:
            print(e, 'error occurred')

        self.tweet()

    def tweet(self):
        # 内容の決定
        img_filename = self.dst_filename
        message = "HACK TIME!!\n" + datetime.now().strftime('%Y/%m/%d %p%I:%M')

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
