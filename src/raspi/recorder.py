#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
import wave
import os
from time import sleep
from raspi import gesture

class Recorder(object):
    def __init__(self):
        self.wf = None

    def callback(self, in_data, frame_count, time_info, status):
        self.wf.writeframes(in_data)
        return (None, pyaudio.paContinue)

    def judge_finish(self):
        while True:
            class_name = gesture.judge()
            if class_name != 'Recorder':
                break
            sleep(0.05)

    def action(self):
        print('record action')

        FORMAT = pyaudio.paInt16
        CHANNELS = 1        #モノラル
        RATE = 44100        #サンプルレート
        CHUNK = 2**9       #データ点数
        RECORD_SECONDS = 5 #録音する時間の長さ
        WAVE_OUTPUT_FILENAME = os.path.abspath(os.path.dirname(__file__)) + '/../../resource/record.wav'

        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        input_device_index=2,   #デバイスのインデックス番号
                        frames_per_buffer=CHUNK)
        print ("recording...")

        frames = []
        while True:
            class_name = gesture.judge()
            #if class_name != 'Recorder':
            if len(frames) > 500:
                break
            data = stream.read(CHUNK)
            frames.append(data)
        print ("finished recording")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        # self.wf = wave.open(os.path.abspath(os.path.dirname(__file__)) + '/../../resource/record.wav', 'w')
        # self.wf.setsampwidth(2)
        # self.wf.setframerate(44100)
        # self.wf.setnchannels(1)
        #
        # p = pyaudio.PyAudio()
        #
        # input_device_index = 2
        #
        # stream = p.open(
        #     format = p.get_format_from_width(self.wf.getsampwidth()),
        #     channels = self.wf.getnchannels(),
        #     rate = self.wf.getframerate(),
        #     input_device_index = input_device_index,
        #     frames_per_buffer=1024,
        #     input = True,
        #     stream_callback = self.callback
        #     )
        #
        # stream.start_stream()
        #
        # self.judge_finish()
        #
        # stream.stop_stream()
        # stream.close()
        #
        # p.terminate()
        # self.wf.close()
