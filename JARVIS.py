import webbrowser
import sys
import speech_recognition as sr
import openai
import os.path
# ------------------------------
import pyttsx3
engine = pyttsx3.init()
#engine.say("Текст")
#engine.tunAndWait()
#------------------------------
from dotenv import load_dotenv as ld

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

def ai_responce(my_task):
    copletion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", messages=[{"role": "user", "content": my_task}]
    )
    return copletion


def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


talk("Да, сер")


def command():
    global r
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
    except sr.UnknownValueError:
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
    else:
        # print(handle_input(input("You: ")).choices[0].message.content)
        try:
            ai_res = ai_responce(ar_task).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk("Произошла ошибка, пробую еще раз")
            try:
                ai_res = ai_responce(ar_task).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk("Не могу обработать ответ, попробуйте еще раз")
        except openai.error.RateLimitError:
            talk("Попробуй через 20 секунд еще раз")
            r.pause_threshold = 20
        except:
            talk("Упс")









while True:
    make_something(command())
