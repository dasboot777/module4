import random
import speech_recognition as sr
recognizer = sr.Recognizer()
spisok_privetstviy = ["Здравствуйте", "Привет", "Как дела?", "Салют!", "Приветствую!", "И тебе привет...", "И вам не хворать"]

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь...")

        speech = recognizer.listen(source)
        speech_to_text = recognizer.recognize_google(speech, language="ru_RU")
        print(f"Вы сказали:{speech_to_text}")

        if speech_to_text.capitalize() == "Привет":
            print(random.choice(spisok_privetstviy))
            break
