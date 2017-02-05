#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import pyaudio
import time
from raspi import gesture
from raspi import led

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BoneSound :
    def __init__(self):
        # チャンク数を指定
        self.CHUNK = 1024
        # self.FILENAME = os.path.abspath(os.path.dirname(__file__)) + '/../../resource/decision1.wav'
        self.FILENAME = '/home/pi/koi.wav'

    # play sound
    def action(self):
        wf = wave.open(self.FILENAME, "rb")

        # LED用の設定
        led_instance = led.LED()

        # PyAudioのインスタンスを生成
        pyaudio_instance = pyaudio.PyAudio()
        # Streamを生成
        """
         format: ストリームを読み書きする際のデータ型
         channels: モノラルだと1、ステレオだと2、それ以外の数字は入らない
         rate: サンプル周波数
         output: 出力モード
        """
        stream = pyaudio_instance.open(
            format=pyaudio_instance.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)

        led_instance.blue_led_on()
        print("Sound Playing")
        # データを1度に1024個読み取る
        data = wf.readframes(self.CHUNK)

        # 実行
        while data != b'' or data is None:
            if gesture.judge() is None:
                break
            stream.write(data)
            data = wf.readframes(self.CHUNK)

        stream.stop_stream()
        stream.close()

        pyaudio_instance.terminate()
        led_instance.blue_led_off()
        led_instance.cleanup()
