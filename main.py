from speech.speech import *

while True:
    # старт записи речи с последующим выводом распознанной речи 
    voice_input = record_and_recognize_audio()
    print(voice_input)