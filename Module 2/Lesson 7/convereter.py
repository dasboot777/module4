from  gtts import gTTS

# f = open("test.txt", "w")#создаем файл
f = open("test.txt", "r", encoding="utf-8")#открываем файл, поддержка кирилицы
text = f.read()#читаем файл в переменную
print(text)
f.close()#закрываем файл
#конвертируем текст в аудио mp3
# tts = gTTS(text=text, lang="en")
tts = gTTS(text=text, lang="ru")
tts.save("privet2.mp3")#сохраняем в файл

