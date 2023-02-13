import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import GoogleNews


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace('jarvis', '')
                talk(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %p')
        talk('The time right now is' + time)
        print(time)
    elif 'wikipedia' or 'who is' or 'what is' or 'tell me about' in command:
        object_of_question = command.replace('wikipedia' or 'who is' or 'tell me about', '')
        info = wikipedia.summary(object_of_question, 3)
        print(info)
        talk(info)
    elif 'joke' or 'jokes' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'news' in command:
        googlenews = GoogleNews()
        googlenews.get_news(command)
        print(googlenews)
        talk(googlenews)
while True:
    run_jarvis()
