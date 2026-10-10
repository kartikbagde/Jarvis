import speech_recognition as sr
import os

contacts = {
    "mom": "9876543210",
    "dad": "9123456780",
    "brother": "9988776655",
    "friend": "9000011111"
}


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower().strip()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""


def call_contact(name):

    if name in contacts:
        number = contacts[name]

        print(f"Calling {name}...")
        print(f"Number: {number}")

        os.system(f'start "" "tel:{number}"')

    else:
        print(f"I don't have a contact named {name}.")


while True:

    command = listen()

    if not command:
        continue

    if command == "call":

        print("Who do you want to call?")

        name = listen()

        if name:
            call_contact(name)

    elif command.startswith("call "):

        name = command.replace("call ", "").strip()

        call_contact(name)

    elif command == "exit" or command == "stop":

        print("Calling assistant stopped.")
        break

    else:

        print("Say something like: Call Mom")