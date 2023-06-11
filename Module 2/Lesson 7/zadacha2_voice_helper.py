import random
import speech_recognition as sr
recognizer = sr.Recognizer()
spisok_filmov = ["Здравствуйте, я ваша тетя", "Экипаж", "Свадьба в Малиновке", "Бриллиантовая рука", "Тот самый Мюнхгаузен", "Королева бензоколонки", "Свой среди чужих, чужой среди своих"]

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь...")

        speech = recognizer.listen(source)
        speech_to_text = recognizer.recognize_google(speech, language="ru_RU")
        print(f"Вы сказали:{speech_to_text}")

        if speech_to_text.capitalize() == "Фильм":
            print(f"Советую вам посмотреть художественный фильм: {random.choice(spisok_filmov)}")
            break