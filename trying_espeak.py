from espeak import espeak

espeak.set_voice("ru")
espeak.synth("где хакер")

while espeak.is_playing:
    pass

