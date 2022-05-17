import re
import pyttsx3
import speech_recognition as sr


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")
    return engine


def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text


def indentify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def main():

    engine = initialize_engine()

    engine.say("¿Cual es tu nombre?")
    engine.runAndWait()

    r = sr.Recognizer()

    text = recognize_voice(r)
    name = indentify_name(text)

    if name:
        engine.say("Bienvenido a tu nuevo asistente de voz {}, mi nombre es Puri".format(name))
    else:
         engine.say("No te he entendido")
    engine.runAndWait()


if __name__ == '__main__':
    main()
