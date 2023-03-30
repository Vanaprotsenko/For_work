from speech.speech import *
from response.hello import*






while True:
    #старт записи речи с последующим выводом распознанной речи 
    voice_input = record_and_recognize_audio()
    print(voice_input)
    
    for i in pharse_list:
        for req in i.request:
            if req in voice_input:
                i.response(voice_input)
    tts_engine.runAndWait()
    