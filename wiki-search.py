import pyttsx3
import wikipedia

engine = pyttsx3.init()

def speak(arg):
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')

    engine.setProperty('rate', 160)
    engine.setProperty('volume', 2)
    engine.setProperty('voice', voices[0].id)

    engine.say(arg)
    engine.runAndWait()


while True:
    user_inp = input("> ")
    speak('Searching...')
    results = wikipedia.summary(user_inp, sentences=2)
    print(f"Searching: {user_inp}")
    speak("According to Wikipedia: ")
    print(f"Result: {results}")
    speak(results)
