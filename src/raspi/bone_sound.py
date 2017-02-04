#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import pyaudio
import time

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BoneSound :
  def __init__(self):
    # チャンク数を指定
    self.CHUNK = 1024
    self.FILENAME = "../../resource/decision1.wav"
    self.wf = wave.open(self.FILENAME, "rb")

    # PyAudioのインスタンスを生成
    self.pyaudio_instance = pyaudio.PyAudio()
    # Streamを生成
    """
     format: ストリームを読み書きする際のデータ型
     channels: モノラルだと1、ステレオだと2、それ以外の数字は入らない
     rate: サンプル周波数
     output: 出力モード
    """
    self.stream = self.pyaudio_instance.open(
      format=self.pyaudio_instance.get_format_from_width(self.wf.getsampwidth()),
      channels=self.wf.getnchannels(),
      rate=self.wf.getframerate(),
      output=True)

  # play sound
  def action(self):
    print("Sound Playing")
    # データを1度に1024個読み取る
    data = self.wf.readframes(self.CHUNK)

    # 実行
    while data != b'':
      self.stream.write(data)
      data = self.wf.readframes(self.CHUNK)

    self.stream.stop_stream()
    self.stream.close()

    self.pyaudio_instance.terminate()