AF1_SeyyedHosseinSeyyedi
The Language Detector and Translator:
For AF1 challenge to detect the language of the input sentence I have created the Detect_And_Translate_Assistant.
This program consists on 3 major functions:
1-detect_language:
This function uses the langid library to detect the language of the input sentence which is the main problem of AF1 Challenge
2-translator:
The first added function that translates the input sentence to the user's language of choice.
Note that this function relies on googletrans library and the users have to write the language of choice according to the style of the library
3-text_to_speech:
The second added function which uses gTTS(Google text to speech) to create an audio of the input system which then will be saved to you local device and played

Finally the Aio_AF1 function uses the capabilities of these 3 functions to do the totality of the program

You can further read about the langid,gTTS and googletrans from the following links

https://github.com/saffsd/langid.py
https://gtts.readthedocs.io/en/latest/
https://pypi.org/project/googletrans/