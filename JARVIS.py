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
    pass


command()
