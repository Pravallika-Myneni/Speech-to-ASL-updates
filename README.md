# Audio to American Sign Language
A python based translator that converts speech (english) to american sign language using animations. 

Contents
========

* [Project Breakdown](#pb)
* [How I built the translator](#how)
* [Steps to use the translator](#use)
* [Potential next steps](#next)

<a name= "pb"></a>
## Project Breakdown
1. Converting speech to text 
2. Analyze the grammar of the text and establish relation between words
3. Generate animation for the sign language translation

<a name="how"></a>

## Steps to use the translator
Step 1: Clone this repository on your system. [Here's a guide](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)

Step 2: Install the required libraries from requirements.txt
```shell
pip3 install -r requirements.txt
```

Step 3: Run the application using the following command in command prompt
```shell
python app.py
```

Step 4: Give the voice/text input and the animation of its asl translation will be available as ``` translation_to_asl.mp4``` after the execution is completed

## How I built the translator
1. Converted speech to text using PyAudio and SpeechRecognition modules
2. Applied NLP processing to understand the structure of words and filter the words in the sentence which can be signed using ASL using NLTK module
3. Generated the signing animation for translation of each word in the filtered words
4. Used MoviePy module to concatenate clips of animations of all words

<a name="use"></a>


<a name="next"></a>
## Potential next steps
* Integrating the translator into an application
* Support other languages
