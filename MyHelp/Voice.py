# -*- coding: utf-8 -*-
import pyttsx


def playVoice():

    tts = pyttsx.Create()
    tts.GetVoiceNames()
    tts.Speak('中国人民共和国')
playVoice()