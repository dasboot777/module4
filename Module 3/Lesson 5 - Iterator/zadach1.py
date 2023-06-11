class MyFile:
    def __init__(self, filename, mode, encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with MyFile("test.txt", "w", encoding="utf-8") as file:#создаем экземпляр класса MyFile - вводим имя файла, режим доступа, тип кодировки
    file.write("Открываем файл и делаем запись этого текста")
    print(f"Проверка: файл закрыт - {file.closed}. Файл все еще открыт (работает контекстный менеджер)")
print(f"Проверка: файл закрыт - {file.closed}. Файл автоматически закрыт (контекстный менеджер завершил работу)")
