
print("Language Codes")
#Refer to this link for more language codes - https://developers.google.com/admin-sdk/directory/v1/languages
print("Hindi: hi")
print("English: en")

lang = input('Choose input audio language code : ')
translate_lang = input("Choose output audio language code: ")
print("")

#Converting Speech to Text

from IPython.display import Audio, display
import speech_recognition as sr
from gtts import gTTS
import os
def transcribe_wav(filename,language="en-US"):

  # Create a new Recognizer object and assign it to r
  r = sr.Recognizer()

  try:
    with sr.AudioFile(filename) as source:
      audio = r.record(source)

      # Use recognize_google to convert audio to text (assuming Google API enabled)
      text = r.recognize_google(audio,language=lang)
      return text
  except sr.UnknownValueError:
    print("Speech could not be understood.")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  return None

filename = "hin_0007.wav"
display(Audio(filename, autoplay=True))


transcribed_text = transcribe_wav(filename,lang)
print("")
if transcribed_text:
  print("Transcription:", transcribed_text)
  print("")
else:
  print("Transcription failed.")


# Translating Text to Text

from deep_translator import GoogleTranslator
to_translate = transcribed_text

translated = GoogleTranslator(source='auto', target=translate_lang).translate(to_translate)
print("Translaion: "+translated)
print("")

#Converting Translated text to speech


# to speech conversion
from gtts import gTTS
from IPython.display import Audio, display

# The text that you want to convert to audio
mytext = translated

# Language in which you want to convert
language = 'hi'

""" Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
"""
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file
myobj.save("speech.mp3")

display(Audio('speech.mp3', autoplay=False))