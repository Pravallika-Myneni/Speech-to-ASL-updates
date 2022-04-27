import os 
import speech_recognition as sr

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

from moviepy.editor import *


# List of all asl sign animations available in our dataset
PATH = "C:/Users/Pravallika Myneni/Desktop/Work/Personal-Projects/Speech_to_ASL/assets/"
files_of_asl_signs_avbl = os.listdir(PATH)

def main():
    
    """  1. User chooses text or speech input
      2. If Speech: 
      3. Convert Speech to text
      go to step 5
      4. Else text:
      5. Analyze grammar and understand the connection of words in the text
      6. Generation of sign language with signing avatar """

    choice = input("press t if you want to give text input or press s for Speech input : ").lower()
    #print(choice)
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
                text = "Can't hear you"
        #print(text)
    elif(choice == 't'):
        text = input("Enter sentence : ")
    else:
        return
    # Standardizing by converting sentence to lower case
    text = text.lower()

    # Tokenizing the sentence
    ## tokenizing = breaking down the sentence into small chunks
    words = word_tokenize(text)


    # Getting the parts of speech of words in the given text
    ## MD represents modal (could, will)
    ## VBP, VBZ and VBG represent Present tense not 3rd person singular, Present tense with 3rd person singular and verb gerund (Ex: speaking) respectively
    ## VBD and VBN denote past tense and past particle respectively
    tagged = nltk.pos_tag(words)

    # Counting the tense forms in the statement for futher predicting the probable tense of statement
    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"])
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
    tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])

    # Removing stopwords and applying lemmatization to tokens

    ## List of stopwords that will be removed
    stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])

    lr = WordNetLemmatizer()
    filtered_text = []
    for w,p in zip(words,tagged):
        if w not in stop_words:
            if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
                    filtered_text.append(lr.lemmatize(w,pos='v'))
            elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
                filtered_text.append(lr.lemmatize(w,pos='a'))
            else:
                filtered_text.append(lr.lemmatize(w))

    # Adding the specific word to specify tense
    words = filtered_text
    temp=[]
    for w in words:
        if w=='I':
            temp.append('Me')
        else:
            temp.append(w)
    words = temp

    probable_tense = max(tense,key=tense.get)

    if probable_tense == "past" and tense["past"]>=1:
        temp = ["Before"]
        temp = temp + words
        words = temp
    elif probable_tense == "future" and tense["future"]>=1:
        if "Will" not in words:
                temp = ["Will"]
                temp = temp + words
                words = temp
        else:
            pass
    elif probable_tense == "present":
        if tense["present_continuous"]>=1:
            temp = ["Now"]
            temp = temp + words
            words = temp

    words = [word.capitalize() for word in words]
    ### print(words)

    # What if animation for asl sign conversion for one or more of the words is not available
    ## Then split the word into alphabets


    filtered_text = []
    for w in words:
        path = w + ".mp4"

        if path not in files_of_asl_signs_avbl :
            for c in w:
                filtered_text.append(c)
        else:
            filtered_text.append(w)
    words = filtered_text
    print(words)

    translated_file_paths = []
    for word in words:
        curr = PATH + word + '.mp4'
        translated_file_paths.append(curr)
    #print(translated_file_paths)

    translated_clips = []

    for file_path in translated_file_paths:
        clip =  VideoFileClip(file_path)
        translated_clips.append(clip)

    final = concatenate_videoclips(translated_clips)
    final.write_videofile("translation_to_asl.mp4")

    return 

main()

