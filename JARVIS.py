import webbrowser
import sys
import speech_recognition as sr

# ------------------------------
import pyttsx3
engine = pyttsx3.init()
#engine.say("Текст")
#engine.tunAndWait()
#------------------------------


def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


talk("Да, сер")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        # print(1)+
        audio = r.listen(source)
        # print(2)
    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Ты: " + task)
    except sr.UnknownValueError():
        talk("Я вас не зрозумів")
        task = command()
    return task


def make_something(ar_task):
    # if ("Открой" and "сайт") in ar_task:
    if ("Открой" and "сайт") in ar_task:
        talk("ok")
        url = "https://youtube.com"
        webbrowser.open(url)
    elif "стоп" in ar_task:
        talk("Good bye")
        sys.exit()
    elif "имя" in ar_task:
        talk("Мое имя Джарвис")



while True:
    make_something(command())
