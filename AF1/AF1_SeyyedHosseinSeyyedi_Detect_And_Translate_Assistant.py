from langdetect import detect
from gtts import gTTS
import langid
import os
from googletrans import Translator

def detect_language(sentence):
    # Use langid to identify the language
    lang, _ = langid.classify(sentence)
    return lang

def text_to_speech(text, lang):
    #use Google text to speech to read the audio
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3") 

def translator(sentence):
    '''a universal translator that will trnaslate the input to any language
    use the first two letters of the destination language such as fa for farsi and ja for japanese'''
    translator = Translator()
    translation = translator.translate(sentence, src=detect_language(sentence), dest=input('enter the destination language'))
    return translation.text

def Aio_AF1():
    sentence = input("Enter a sentence: ")
    
    detected_language = detect_language(sentence)

    
    if detected_language:
        print("Text:",sentence)
        print("Detected language:", detected_language)
        print(translator(sentence))
        text_to_speech(sentence, detected_language)        
    else:
        print("Language detection failed.")

Aio_AF1()