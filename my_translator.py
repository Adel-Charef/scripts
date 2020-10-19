#!/usr/bin/env python

from googletrans import Translator
import pyttsx3
import sys

translator = Translator()
play = pyttsx3.init()

text = input("Enter Text: ")
src = input("Enter the src lang: ")
dest = input("Enter the dest lang: ")
translated = translator.translate(text, src=src, dest=dest)
print("----------------------------------")
print(translated.text)
print("----------------------------------")
sound = input("Would you like to play sound (yes/no): ")
if sound == "yes" or sound == "y":
    play.setProperty('rate', 130)
    play.say(translated.text)
    play.runAndWait()
else:
    sys.exit()
