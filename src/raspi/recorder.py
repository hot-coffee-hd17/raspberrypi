#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
import sys
import time
import wave
from multiprocessing import Process

RATE = 44100 # サンプリングレート、マイク性能に依存
CHUNK = 1024

class Recorder(object):
    def __init__(self):
        # pyaudio
        self.p = pyaudio.PyAudio()

        # マイクからデータ取得
        self.stream = self.p.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = RATE,
            input = True,
            frames_per_buffer = CHUNK
            )

        # 録音データを保存する
        self.all = []

    def record(self):
        for i in range(0, int(RATE / CHUNK * 3)):
            data = self.stream.read(CHUNK)
            self.all.append(data)

    def action(self):
        print('record!')
        
        self.record()
         
        self.stream.close()
        data = b''.join(self.all)
        out = wave.open('mono.wav','w')
        out.setnchannels(1) #mono
        out.setsampwidth(2) #16bits
        out.setframerate(RATE)
        out.writeframes(data)
        out.close()
         
        self.p.terminate()
