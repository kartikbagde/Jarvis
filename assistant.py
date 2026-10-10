import speech_recognition as sr
import webbrowser as wb
import os

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""


def execute(command):

    if "open youtube" in command:
        wb.open("https://youtube.com")

    elif "open google" in command:
        wb.open("https://google.com")

    elif "open notepad" in command:
        os.system("notepad")

    elif "open file" in command or "open explorer" in command:
        os.startfile(".")

    elif "open camera" in command:
        os.system("start microsoft.windows.camera:")

    elif "open mysql" in command or "open workbench" in command:
        os.system("start mysqlworkbench")

    elif "open microsoft store" in command or "open store" in command:
        os.system("start ms-windows-store:")

    elif "open vs code" in command or "open visual studio code" in command:
        os.system("code")

    elif "open claude" in command:
        os.system("start claude")

    elif "open whatsapp" in command:
        os.system("start whatsapp:")

    elif "exit" in command or "stop" in command:
        print("Goodbye!")
        return False

    else:
        print("I don't know that command.")

    return True


while True:
    command = listen()

    if command:
        if not execute(command):
            break