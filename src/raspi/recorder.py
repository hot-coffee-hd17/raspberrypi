#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
import wave
from raspi import sensor

class Recorder(object):
    def __init__(self):
        self.wf = None

    def callback(self, in_data, frame_count, time_info, status):
        self.wf.writeframes(in_data)
        return (None, pyaudio.paContinue)

    def judge_finish(self):
        while True:
            # センサの値取得
            sensor_values = sensor.get_values()
            
            # 終了ジェスチャーを検知
            # TODO ここに終了を検知するコードを追加
            break

        # 今は3秒スリープするだけ
        import time
        time.sleep(3)

    def action(self):
        print('record action')

        self.wf = wave.open('record.wav', 'w')
        self.wf.setsampwidth(2)
        self.wf.setframerate(44100)
        self.wf.setnchannels(2)

        p = pyaudio.PyAudio()

        input_device_index = 0

        stream = p.open(
            format = p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            input_device_index = input_device_index,
            input = True,
            stream_callback = self.callback
            )

        stream.start_stream()

        self.judge_finish()
        
        stream.stop_stream()
        stream.close()

        p.terminate()
        self.wf.close()
