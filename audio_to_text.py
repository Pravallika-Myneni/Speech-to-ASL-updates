import os 
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print("Answer: "+ text) 
        except:
            print("Sorry, I did not get that")
            text = ""
    return text

text = speech_to_text()
print(text)