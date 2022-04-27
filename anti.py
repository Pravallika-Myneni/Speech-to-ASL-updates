import os 
import speech_recognition as sr

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

import cv2

#from audio_to_text import speech_to_text

from sentence_to_words import sentence_to_words

from words_to_animation import play_video

def main():
    
    ### 1. User chooses text or speech input
    ### 2. If Speech: 
    ### 3. Convert Speech to text
    ### go to step 5
    ### 4. Else text:
    ### 5. Analyze grammar and understand the connection of words in the text
    ### 6. Generation of sign language with signing avatar

    choice = input("press t if you want to give text input or press s for Speech input : ").lower()
    
    if(choice == 's'):
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

    elif(choice == 't'):
        text = input("Enter sentence : ")
    else:
        return
    words = sentence_to_words(text)

    for word in words:
        file = "C:\\Users\\Pravallika Myneni\\Desktop\\Work\\Personal-Projects\\Speech_to_ASL\\assets\\" + word +".mp4"
        play_video(file)
    return 
main()

