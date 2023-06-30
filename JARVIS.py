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
        audio = r.listen(source)



    task = r.recognize_google(audio, language="ru-RU").lower()
    print("You: " + task)

    return task


def make_something(ar_task):
    if "Открой" and "сайт" in ar_task:
        talk("ok")
        url = "https://youtube.com"
        webbrowser.open(url)




while True:
    make_something(command())