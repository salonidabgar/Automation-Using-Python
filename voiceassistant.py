import pyttsx3
import speech_recognition as sr
import webbrowser
import pyjokes
import datetime

def sptext():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recogniser.adjust_for_ambient_noise(source)
        audio = recogniser.listen(source)
        try:
            print("Recognising...")
            data = recogniser.recognize_google(audio)
            # print(data)
            return data
        except sr.UnknownValueError:
            print("Did Not Understood:( Speak Again!")

# sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()

# speechtx("Hello Welcome Saloni. This is your first voice assistant")

if __name__ == '__main__':
    if sptext().lower() == "hey siri":
        data = sptext().lower()
        if "youtube" in data:
            webbrowser.open("https://www.youtube.com/watch?v=Vh0xw9t88SA")
        elif "your age" in data:
            age = "i am 10 years old"
            speechtx(age)
        elif "time" in data:
            time = datetime.datetime.now().strftime('%I%M%p')
            speechtx(time)
        elif "joke" in data:
            joke = pyjokes.get_joke(language='en', category='neutral')
            speechtx(joke)

    else:
        print("Sorry can't hear.Try Again!")


